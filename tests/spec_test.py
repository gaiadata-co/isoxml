''' Test cases for isoxml.spec '''
from isoxml import spec

def test_init():
    '''test init which may raise ISOXMLInitException'''
    spec.init()
    assert True
