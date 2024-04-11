''' Test cases for isoxml.entity '''
import unittest

from isoxml import entity
from isoxml import exception

valid = {}

valid["ISO11783_TaskData"] = """<ISO11783_TaskData
        VersionMajor="4"
        VersionMinor="0"
        ManagementSoftwareManufacturer="GaiaData"
        ManagementSoftwareVersion="1.0.0"
        DataTransferOrigin="TaskController">
    </ISO11783_TaskData>"""

valid["AFE"] = """ <AFE A="foo.txt" B="True" C="GLN" D="txt" ></AFE>"""

class TestEntity(unittest.TestCase):
    ''' Test cases for isoxml.entity '''
    def test_taskdata_blank_fail(self):
        ''' Test that missing required fields in taskdata raises an exception '''
        data = "<ISO11783_TaskData> </ISO11783_TaskData>"
        with self.assertRaises(exception.ISOXMLParseException):
            entity.Entity(data)

    def test_taskdata(self):
        ''' Test that taskdata is parsed correctly '''

        for tag, xml in valid.items():
            e = entity.Entity(xml)
            assert e.tag() == tag
