class ISOXMLException(Exception):
    ''' Base class for all exceptions in the isoxml package '''

class ISOXMLParseException(ISOXMLException):
    ''' Exception raised when there is an error parsing the ISOXML '''

class ISOXMLInitException(ISOXMLException):
    ''' Exception raised when there is an error initializing the ISOXML '''

