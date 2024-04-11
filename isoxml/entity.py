"""A library for parsing ISOXML files (ISO 11783:10)

Typical usage example:

import isoxml

taskdata = isoxml.entity.Entity("<ISO11783_TaskData> ... </ISO11783_TaskData>")

"""
import re
import xml.etree.ElementTree
from . import exception
from . import spec

class Entity:
    '''
    Entity represents an ISOXML entity with its attributes and child entities

    We do not create a separate class for each entity type, instead we use a single Entity class
    and parse the XML. Based on the type of the entity and its associated spec, we populate the
    attributes and child entities.

    '''

    # we start by initializing the spec
    spec = spec.init()

    def __init__(self, data):
        self.element = xml.etree.ElementTree.fromstring(data)
        self.parse()

    def tag(self):
        ''' Returns the tag of the entity (e.g. ISO11783_TaskData)'''
        return self.element.tag

    def parse(self):
        ''' Parse the XML and populate the attributes and child entities based on the spec '''
        if self.element.tag in Entity.spec:
            _map = Entity.spec[self.element.tag]["map"]
            required = Entity.spec[self.element.tag]["required"]
            ctags = Entity.spec[self.element.tag]["ctags"]

            pattern = re.compile(r'(?<!^)(?=[A-Z])')

            # populate the attributes
            for k, v in self.element.attrib.items():
                if k in _map:
                    k = _map[k]

                self.__dict__[pattern.sub('_', k).lower()] = v

            # check if all required attributes are present
            for k in required:
                if pattern.sub('_', k).lower() not in self.__dict__:
                    msg = f"Required attribute {k} not found in {self.element.tag}"
                    raise exception.ISOXMLParseException(msg)

            # recursively find and parse child entities for child tags
            for child_tag in ctags:
                children = self.element.findall(child_tag)

                if children:
                    self.__dict__[child_tag] = [Entity(xml.etree.ElementTree.tostring(e)) for e in children]
        else:
            raise exception.ISOXMLParseException(f"Unknown tag {self.element.tag}")

    def __repr__(self):
        return f"{self.element.tag} {self.__dict__}"

    def __str__(self):
        return f"{self.element.tag} {self.__dict__}"
