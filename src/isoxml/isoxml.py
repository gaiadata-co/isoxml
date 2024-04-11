"""A library for parsing ISOXML files (ISO 11783:10)

Typical usage example:

import isoxml
import xml

isoxml.Entity.init_spec() ### Initializing the spec is REQUIRED

data = "<ISO11783_TaskData> ... </ISO11783_TaskData>"
element = xml.etree.ElementTree.fromstring(data)
entity = isoxml.Entity(element)

"""
import re
from isoxml import spec

class Entity:
    '''
    Entity represents an ISOXML entity with its attributes and child entities

    We do not create a separate class for each entity type, instead we use a single Entity class
    and parse the XML. Based on the type of the entity and its associated spec, we populate the
    attributes and child entities.

    '''
    def __init__(self, element):
        self.element = element
        self.parse()

    @classmethod
    def init_spec(cls):
        cls.spec = spec.init_spec()

    def tag(self):
        return self.element.tag
    
    def parse(self):
        if self.element.tag in Entity.spec:
            _map = Entity.spec[self.element.tag]["map"]
            required = Entity.spec[self.element.tag]["required"]
            ctags = Entity.spec[self.element.tag]["ctags"]

            pattern = re.compile(r'(?<!^)(?=[A-Z])')
             
            for k, v in self.element.attrib.items():
                if k in _map:
                    k = _map[k]
                
                self.__dict__[pattern.sub('_', k).lower()] = v
            
            for k in required:
                assert pattern.sub('_', k).lower() in self.__dict__, f"Required attribute {k} not found in {self.element.tag}"
            
            for child_tag in ctags:
                children = self.element.findall(child_tag)
                if children:
                    self.__dict__[child_tag] = [Entity(e) for e in children]
        else:
            print(f"Unknown tag {self.element.tag}")

    def __repr__(self):
        return f"{self.element.tag} {self.__dict__}"

    def __str__(self):
        return f"{self.element.tag} {self.__dict__}"