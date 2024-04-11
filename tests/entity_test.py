''' Test cases for isoxml.entity '''
import pytest

from isoxml import entity, exception

valid = {}

valid["ISO11783_TaskData"] = """<ISO11783_TaskData
        VersionMajor="4"
        VersionMinor="0"
        ManagementSoftwareManufacturer="GaiaData"
        ManagementSoftwareVersion="1.0.0"
        DataTransferOrigin="TaskController">
    </ISO11783_TaskData>"""

valid["AFE"] = """ <AFE A="foo.txt" B="True" C="GLN" D="txt" ></AFE>"""
valid["PNT"] = '<PNT A="10" C="49.3682793876954" D="9.55990880103963" />'
valid["LSG"] = """
<LSG A="1">
                <PNT A="10" C="49.3682793876954" D="9.55990880103963" />
            </LSG>
"""

full = """
<ISO11783_TaskData VersionMajor="3" VersionMinor="0" ManagementSoftwareManufacturer="GaiaData"
    ManagementSoftwareVersion="1.0.1" DataTransferOrigin="1">
    <CTR A="CTR1" B="Not defined" />
    <FRM A="FRM1" B="Default farm" I="CTR1" />
    <PFD A="PFD1" C="Test Farm" D="49100" F="FRM1" E="CTR1">
        <PLN A="1" B="Field boundary" C="49100">
            <LSG A="1">
                <PNT A="10" C="49.3682793876954" D="9.55990880103963" />
                <PNT A="10" C="49.3683205752992" D="9.55984383748131" />
                <PNT A="10" C="49.3683337313559" D="9.5598126937734" />
                <PNT A="10" C="49.368384511624" D="9.55968525294447" />
                <PNT A="10" C="49.3684243114024" D="9.55952354968232" />
                <PNT A="10" C="49.3684454371798" D="9.55938154837636" />
                <PNT A="10" C="49.3684670454333" D="9.55913998366188" />
                <PNT A="10" C="49.3684652391959" D="9.55911360323687" />
                <PNT A="10" C="49.3684644881577" D="9.55908628976923" />
                <PNT A="10" C="49.3687009152318" D="9.55872189980868" />
                <PNT A="10" C="49.368735760087" D="9.55877504548091" />
                <PNT A="10" C="49.3687897177012" D="9.55886606100872" />
                <PNT A="10" C="49.3688626220258" D="9.55898911497108" />
                <PNT A="10" C="49.3691263611712" D="9.55946684931311" />
                <PNT A="10" C="49.3696721216266" D="9.56054425120233" />
                <PNT A="10" C="49.3696929491079" D="9.56059280630861" />
                <PNT A="10" C="49.3698058159993" D="9.5608559833575" />
                <PNT A="10" C="49.3698572161761" D="9.56101061478527" />
                <PNT A="10" C="49.3699393799723" D="9.56125789727029" />
                <PNT A="10" C="49.369988889421" D="9.56143890777174" />
                <PNT A="10" C="49.3700082673176" D="9.56150981656358" />
                <PNT A="10" C="49.36998234145" D="9.56160716895198" />
                <PNT A="10" C="49.3698586130544" D="9.56171582858403" />
                <PNT A="10" C="49.3689317224255" D="9.56252977803224" />
                <PNT A="10" C="49.3688248691087" D="9.56263060982657" />
                <PNT A="10" C="49.3686957597975" D="9.56275240085093" />
                <PNT A="10" C="49.3684521871728" D="9.56300836076855" />
                <PNT A="10" C="49.3684477308482" D="9.56301304286879" />
                <PNT A="10" C="49.3682144959614" D="9.56325813715614" />
                <PNT A="10" C="49.3679625358832" D="9.56278978397907" />
                <PNT A="10" C="49.3679367506842" D="9.56274397431293" />
                <PNT A="10" C="49.3678280361808" D="9.56256067171969" />
                <PNT A="10" C="49.3677285808708" D="9.56238316392208" />
                <PNT A="10" C="49.3676272533226" D="9.5622084803808" />
                <PNT A="10" C="49.3675811301941" D="9.56214252701246" />
                <PNT A="10" C="49.3673099940951" D="9.56174118684326" />
                <PNT A="10" C="49.3676268005815" D="9.56115877161335" />
                <PNT A="10" C="49.3682793876954" D="9.55990880103963" />
            </LSG>
        </PLN>
    </PFD>
    <PGP A="PGP1" B="Fertilizers" />
    <VPN A="VPN1" B="0" C="0.01" D="2" E="kg/ha" />
    <CPC A="CPC1" B="Fertilizers" />
    <PDT A="PDT1" B="fertilizers" C="PGP1" D="VPN1" E="004B" />
    <TSK A="TSK1" B="OneSoil-2023-04-13" D="FRM1" C="CTR1" E="PFD1" G="1" H="1" J="0">
        <DLT A="DFFF" B="31" />
        <TZN A="0" B="Out of field">
            <PDV A="0006" B="0" C="PDT1" E="VPN1" />
        </TZN>
        <TZN A="1" B="Field">
            <PDV A="0006" B="0" C="PDT1" E="VPN1" />
        </TZN>
        <OTP A="CPC1" />
        <GRD A="49.3673099940951" B="9.55872189980868" C="8.928038554500972e-05"
            D="0.00013874802058033708" E="33" F="30" G="GRD00001" I="2" J="1" />
    </TSK>
</ISO11783_TaskData>
"""

def test_taskdata_blank_fail():
    ''' Test that missing required fields in taskdata raises an exception '''
    data = "<ISO11783_TaskData> </ISO11783_TaskData>"
    with pytest.raises(exception.ISOXMLParseException):
        entity.Entity(data)

def test_entity():
    ''' Test that taskdata is parsed correctly '''

    for tag, xml in valid.items():
        e = entity.Entity(xml)
        assert e.tag() == tag
