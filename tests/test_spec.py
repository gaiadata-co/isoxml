''' Test cases for isoxml.spec '''
import unittest

from isoxml import spec

class TestSpec(unittest.TestCase):
    ''' Test cases for isoxml.spec '''
    def test_init(self):
        '''test init which may raise ISOXMLInitException'''
        spec.init()
        assert True
