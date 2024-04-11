''' ISOXML spec '''

from . import exception

def init():
    ''' Initialize the ISOXML spec '''
    spec = {}

    for tag in tags:
        for x in ["map", "required", "ctags"]:
            if f"{tag}_{x}" not in globals():
                raise exception.ISOXMLInitException(f"Missing {tag} {x} spec")

        _map = globals()[f"{tag}_map"]
        required = globals()[f"{tag}_required"]
        ctags = globals()[f"{tag}_ctags"]

        spec[tag] = {
            "map": _map,
            "required": required,
            "ctags": ctags
        }

    return spec

tags = [
    "AFE", "ASP", "BSN", "CAN", "CAT", "CCG", "CCL", "CCT", "CLD", "CNN",
    "CPC", "CRG", "CTP", "CTR", "CVT", "DAN", "DET", "DLT", "DLV", "DOR",
    "DPD", "DPT", "DVC", "DVP", "FRM", "GAN", "GGP", "GPN", "GRD", "GST",
    "LGP", "LNK", "LSG", "OTP", "OTQ", "OTR", "PAN", "PDT", "PDV", "PFD",
    "PGP", "PLN", "PNT", "PRN", "PTN", "TCC", "TIM", "TLG", "TSK", "TZN",
    "VPN", "WAN", "WKR", "XFC", "XFR", "ISO11783_TaskData", "ISO11783_LinkedList",
]

ISO11783_TaskData_map = {}
ISO11783_TaskData_required = [
    "VersionMajor",
    "VersionMinor",
    "ManagementSoftwareManufacturer",
    "ManagementSoftwareVersion",
    "DataTransferOrigin"
]
ISO11783_TaskData_ctags = [
    "AFE", "BSN", "CCT", "CCG", "CLD", "CTP", "CPC", "CTR", "DVC", "FRM",
    "OTQ", "PFD", "PDT", "PGP", "TSK", "TCC", "VPN", "WKR", "XFR"
]

ISO11783_LinkedList_required = [
    "VersionMajor",
    "VersionMinor",
    "ManagementSoftwareManufacturer",
    "ManagementSoftwareVersion",
    "DataTransferOrigin"
]
ISO11783_LinkedList_map = {
    "VersionMajor": "VersionMajor",
    "VersionMinor": "VersionMinor",
    "ManagementSoftwareManufacturer": "ManagementSoftwareManufacturer",
    "ManagementSoftwareVersion": "ManagementSoftwareVersion",
    "TaskControllerManufacturer": "TaskControllerManufacturer",
    "TaskControllerVersion": "TaskControllerVersion",
    "FileVersion": "FileVersion",
    "DataTransferOrigin": "DataTransferOrigin",
}
ISO11783_LinkedList_ctags = ["LGP"]

AFE_required = ["FilenameWithExtension", "Preserve", "ManufacturerGLN", "FileType"]
AFE_map = {
    "A": "FilenameWithExtension",
    "B": "Preserve",
    "C": "ManufacturerGLN",
    "D": "FileType",
    "E": "FileVersion",
    "F": "FileLength"
}
AFE_ctags = []

ASP_required = ["Start", "Type"]
ASP_map = {"A": "Start", "B": "Stop", "C": "Duration", "D": "Type"}
ASP_ctags = ["PTN"]

BSN_required = ["Id", "Designator", "North", "East", "Up"]
BSN_map = {"A": "Id", "B": "Designator", "C": "North", "D": "East", "E": "Up"}
BSN_ctags = []

CAN_required = []
CAN_map = {
    "A": "CctIdRef",
    "B": "CclIdRef",
    "C": "FreeCommentText",
}
CAN_ctags = ["ASP"]

CAT_required = ["SourceClientName", "UserClientName", "SourceDeviceStructureLabal",
                "UserDeviceStructureLabel", "SourceDeviceElementNumber", "UserDeviceElementNumber",
                "ProcessDataDDI"]
CAT_map = {
    "A": "SourceClientName",
    "B": "UserClientName",
    "C": "SourceDeviceStructureLabal",
    "D": "UserDeviceStructureLabel",
    "E": "SourceDeviceElementNumber",
    "F": "UserDeviceElementNumber",
    "G": "ProcessDataDdi"
}
CAT_ctags = []

CCG_required = ["Id", "Designator"]
CCG_map = {
    "A": "Id",
    "B": "Designator",
}
CCG_ctags = []

CCL_required = ["Id", "Designator",]
CCL_map = {
    "A": "Id",
    "B": "Designator",
}
CCL_ctags = []

CCT_required = ["Id", "Designator", "Scope"]
CCT_map = {"A": "Id", "B": "Designator", "C": "Scope", "D": "CCGIdRef"}
CCT_ctags = ["CCL"]

CLD_required = ["Id", ]
CLD_map = {
    "A": "Id",
    "B": "DefaultColor",
}
CLD_ctags = ["CRG"]

CNN_required = [
    "DeviceIdRef_0",
    "DeviceElementIdRef_0",
    "DeviceIdRef_1",
    "DeviceElementIdRef_1",
]
CNN_map = {
    "A": "DeviceIdRef_0",
    "B": "DeviceElementIdRef_0",
    "C": "DeviceIdRef_1",
    "D": "DeviceElementIdRef_1",
}
CNN_ctags = []

CRG_required = [ "MinimumValue", "MaximumValue", "Color", ]
CRG_map = {
    "A": "MinimumValue",
    "B": "MaximumValue",
    "C": "Color",
}
CRG_ctags = []

CPC_required = ["Id", "Designator"]
CPC_map = {"A": "Id", "B": "Designator"}
CPC_ctags = ["OTR"]

CTP_required = ["Id", "Designator"]
CTP_map = {"A": "Id", "B": "Designator", "C": "PGPIdRef"}
CTP_ctags = ["CVT"]

CTR_required = ["Id", "LastName"]
CTR_map = {
    "A": "Id",
    "B": "LastName",
    "C": "FirstName",
    "D": "Street",
    "E": "POBox",
    "F": "PostalCode",
    "G": "City",
    "H": "State",
    "I": "Country",
    "J": "Phone",
    "K": "Mobile",
    "L": "Fax",
    "M": "Email"
}
CTR_ctags = []

CVT_required = ["Id", "Designator"]
CVT_map = {"A": "Id", "B": "Designator", "C": "PDTIdRef"}
CVT_ctags = []

DAN_required = ["ClientNameValue"]
DAN_map = {"A": "ClientNameValue", "B": "ClientNameMask", "C": "DvcIdRef"}
DAN_ctags = ["ASP"]

DET_required = ["Id", "ObjectId", "Type", "Number", "ParentObjectId"]
DET_map = {
    "A": "Id",
    "B": "ObjectId",
    "C": "Type",
    "D": "Designator",
    "E": "Number",
    "F": "ParentObjectId",
}
DET_ctags = ["DOR"]

DLT_required = ["Ddi", "Method"]
DLT_map = {
    "A": "Ddi",
    "B": "Method",
    "C": "DistanceInterval",
    "D": "TimeInterval",
    "E": "ThresholdMinimum",
    "F": "ThresholdMaximum",
    "G": "ThresholdChange",
    "H": "DetIdRef",
    "I": "VpnIdRef",
    "J": "Pgn",
    "K": "PgnStartBit",
    "L": "PgnStopBit",
}
DLT_ctags = []

DLV_required = ["Ddi", "Value", "DetIdRef"]
DLV_map = {
    "A": "Ddi",
    "B": "Value",
    "C": "DetIdRef",
    "D": "DataLogPgn",
    "E": "DataLogPgnStartBit",
    "F": "DataLogPgnStopBit",
}
DLV_ctags = []

DOR_required = ["Id"]
DOR_map = {"A": "Id",}
DOR_ctags = []

DPD_required = ["ObjectId", "Ddi", "Property", "TriggerMethods"]
DPD_map = {
    "A": "ObjectId",
    "B": "Ddi",
    "C": "Property",
    "D": "TriggerMethods",
    "E": "Designator",
    "F": "DvpObjectId",
}
DPD_ctags = []

DPT_required = ["ObjectId", "Ddi", "Value"]
DPT_map = {
    "A": "ObjectId",
    "B": "Ddi",
    "C": "Value",
    "D": "Designator",
    "E": "DvpObjectId",
}
DPT_ctags = []

DVC_required = ["Id", "ClientName", "StructureLabel", "LocalizationLabel"]
DVC_map = {
    "A": "Id",
    "B": "Designator",
    "C": "SoftwareVersion",
    "D": "ClientName",
    "E": "SerialNumber",
    "F": "StructureLabel",
    "G": "LocalizationLabel",
}
DVC_ctags = ["DET", "DPD", "DPT", "DVP"]

DVP_required = ["ObjectId", "Offset", "Scale", "NumberOfDecimals", "UnitDesignator"]
DVP_map = {
    "A": "ObjectId",
    "B": "Offset",
    "C": "Scale",
    "D": "NumberOfDecimals",
    "E": "UnitDesignator",
}
DVP_ctags = []

FRM_required = ["Id", "Designator"]
FRM_map = {
    "A": "Id",
    "B": "Designator",
    "C": "Street",
    "D": "POBox",
    "E": "PostalCode",
    "F": "City",
    "G": "State",
    "H": "Country",
    "I": "CustomerIdRef"
}
FRM_ctags = []

GAN_required = ["GgnIdRef"]
GAN_map = { "A": "GgnIdRef" }
GAN_ctags = ["ASP", "GST"]

GGP_required = ["Id"]
GGP_map = {
    "A": "Id",
    "B": "Designator",
}
GGP_ctags = ["GPN", "PLN"]

GPN_required = ["Id", "Type"]
GPN_map = {
    "A": "Id",
    "B": "Designator",
    "C": "Type",
    "D": "Options",
    "E": "PropagationDirection",
    "F": "Extension",
    "G": "Heading",
    "H": "Radius",
    "I": "GnssMethod",
    "J": "HorizontalAccuracy",
    "K": "VerticalAccuracy",
    "L": "BsnIdRef",
    "M": "OriginalSrid",
    "N": "NumberOfSwathsLeft",
    "O": "NumberOfSwathsRight",
}
GPN_ctags = ["LSG", "PLN"]

GRD_required = [
    "MinimumNorthPosition",
    "MinimumEastPosition",
    "CellNorthSize",
    "CellEastSize",
    "MaximumColumn",
    "MaximumRow",
    "FileName",
    "GridType"
]
GRD_map = {
    "A": "MinimumNorthPosition",
    "B": "MinimumEastPosition",
    "C": "CellNorthSize",
    "D": "CellEastSize",
    "E": "MaximumColumn",
    "F": "MaximumRow",
    "G": "FileName",
    "H": "FileLength",
    "I": "GridType",
    "J": "TreatmentZoneCode",
}
GRD_ctags = []

GST_required = []
GST_map = {
    "A": "GgpIdRef",
    "B": "GpnIdRef",
    "C": "East",
    "D": "North",
    "E": "PropagationOffset",
}
GST_ctags = [ "ASP" ]

LGP_required = ["Id", "Type"]
LGP_map = {
    "A": "Id",
    "B": "Type",
    "C": "ManufacturerGln",
    "D": "Namespace",
    "E": "Designator",
}
LGP_ctags = ["LNK"]

LNK_required = ["ObjectIdRef", "Value"]
LNK_map = {
    "A": "ObjectIdRef",
    "B": "Value",
    "C": "Designator",
}
LNK_ctags = []

LSG_required = ["Type"]
LSG_map = {
    "A": "Type",
    "B": "Designator",
    "C": "Width",
    "D": "Length",
    "E": "Color",
    "F": "Id",
}
LSG_ctags = ["PNT"]

OTP_required = ["CpcIdRef"]
OTP_map = { "A": "CpcIdRef", "B": "OtqIdRef", }
OTP_ctags = []

OTQ_required = ["Id", "Designator"]
OTQ_map = { "A": "Id", "B": "Designator", }
OTQ_ctags = []

OTR_required = ["OtqIdRef"]
OTR_map = { "A": "OtqIdRef" }
OTR_ctags = []

PAN_required = ["PdtIdRef"]
PAN_map = {
    "A": "PdtIdRef",
    "B": "QuantityDdi",
    "C": "QuantityValue",
    "D": "TransferMode",
    "E": "DetIdRef",
    "F": "VpnIdRef",
    "G": "ProduyctSubTypeIdRef",
}
PAN_ctags = ["ASP"]

PDT_required = ["Id", "Designator"]
PDT_map = {
    "A": "Id",
    "B": "Designator",
    "C": "PgpIdRef",
    "D": "VpnIdRef",
    "E": "QuanityDdi",
    "F": "Type",
    "G": "MixtureRecipeQuantity",
    "H": "DensityMassPerVolume",
    "I": "DensityMassPerCount",
    "J": "DensityVolumePerCount",
}
PDT_ctags = ["PRN"]

PDV_required = ["Ddi", "Value"]
PDV_map = {
    "A": "Ddi",
    "B": "Value",
    "C": "PdtIdRef",
    "D": "DetIdRef",
    "E": "VpnIdRef",
    "F": "ActualCpcIdRef",
    "G": "ElementTypeInstanceValue",
}
PDV_ctags = ["PDV"]

PFD_required = ["Id", "Designator", "Area"]
PFD_map = {
    "A": "Id",
    "B": "Code",
    "C": "Designator",
    "D": "Area",
    "E": "CtrIdRef",
    "F": "FrmIdRef",
    "G": "CtpIdRef",
    "H": "CvtIdRef",
    "I": "FieldIdRef",
}
PFD_ctags = ["PLN", "LSG", "PNT", "GGP"]

PGP_required = ["Id", "Designator"]
PGP_map = {
    "A": "Id",
    "B": "Designator",
    "C": "Type",
}
PGP_ctags = []

PLN_required = ["Type"]
PLN_map = {
    "A": "Type",
    "B": "Designator",
    "C": "Area",
    "D": "Color",
    "E": "Id",
}
PLN_ctags = ["LSG"]

PNT_required = ["Type", "North", "East" ]
PNT_map = {
    "A": "Type",
    "B": "Designator",
    "C": "North",
    "D": "East",
    "E": "Up",
    "F": "Color",
    "G": "Id",
    "H": "HorizontalAccuracy",
    "I": "VerticalAccuracy",
    "J": "FileName",
    "K": "FileLength",
}
PNT_ctags = []

PRN_required = ["PdtIdRef", "QuantityValue"]
PRN_map = {
    "A": "PdtIdRef",
    "B": "QuantityValue",
}
PRN_ctags = []

PTN_required = ["North", "East", "Status"]
PTN_map = {
    "A": "North",
    "B": "East",
    "C": "Up",
    "D": "Status",
    "E": "Pdop",
    "F": "Hdop",
    "G": "NumberOfSatellites",
    "H": "GpsUtcTime",
    "I": "GpsUtcDate",
}

PTN_ctags = []

TCC_required = [
    "FunctionName",
    "Designator",
    "VersionNumber",
    "ProvidedCapabilities",
    "NumberOfBoomsSectionControl",
    "NumberOfSectionsSectionControl",
    "NumberOfControlChannels",
]
TCC_map = {
    "A": "FunctionName",
    "B": "Designator",
    "C": "VersionNumber",
    "D": "ProvidedCapabilities",
    "E": "NumberOfBoomsSectionControl",
    "F": "NumberOfSectionsSectionControl",
    "G": "NumberOfControlChannels",
}
TCC_ctags = []

TIM_required = ["Start", "Type"]
TIM_map = {
    "A": "Start",
    "B": "Stop",
    "C": "Duration",
    "D": "Type",   
}
TIM_ctags = ["PTN", "DLV"]

TLG_required = ["FileName", "Type"]
TLG_map = {
    "A": "FileName",
    "B": "FileLength",
    "C": "Type",
}
TLG_ctags = []

TSK_required = ["Id", "Status"]
TSK_map = {
    "A": "Id",
    "B": "Designator",
    "C": "CtrIdRef",
    "D": "FrmIdRef",
    "E": "PfdIdRef",
    "F": "WkrIdRef",
    "G": "Status",
    "H": "DefaultTreatmentZoneCode",
    "I": "PositionLostTreatmentZoneCode",
    "J": "OutOfFieldTreatmentZoneCode",
}
TSK_ctags = [
    "TZN", "TIM", "OTP", "WAN", "DAN", "CNN",
    "PAN", "DLT", "CAN", "TLG", "GRD", "CAT", "GAN"
]

TZN_required = ["Code"]
TZN_map = {
    "A": "Code",
    "B": "Designator",
    "C": "Color",
}
TZN_ctags = ["PLN", "PDT"]

VPN_required = ["Id", "Offset", "Scale", "NumberOfDecimals"]
VPN_map = {
    "A": "Id",
    "B": "Offset",
    "C": "Scale",
    "D": "NumberOfDecimals",
    "E": "UnitDesignator",
    "F": "CldIdRef",
}
VPN_ctags = []

WAN_required = ["WkrIdRef"]
WAN_map = { "A": "WkrIdRef" }
WAN_ctags = ["ASP"]

WKR_required = ["Id", "LastName"]
WKR_map = {
    "A": "Id",
    "B": "LastName",
    "C": "FirstName",
    "D": "Street",
    "E": "POBox",
    "F": "PostalCode",
    "G": "City",
    "H": "State",
    "I": "Country",
    "J": "Phone",
    "K": "Mobile",
    "L": "LicenseNumber",
    "M": "Email"
}
WKR_ctags = []

XFC_required = []
XFC_map = {}
XFC_ctags = [
    "BSN", "CCT", "CCG", "CLD", "CTP", "CPC", "CTR", "DVC", "FRM",
    "OTQ", "PFD", "PDT", "PGP", "TSK", "VPN", "WKR"
]

XFR_required = ["FileName", "Type"]
XFR_map  = {
    "A": "FileName",
    "B": "Type",
}
XFR_ctags = []
