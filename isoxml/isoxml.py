import re
import sys
import xml.etree.ElementTree as ET
import zipfile

from spec import init_spec

'''
Entity represents an ISOXML entity with its attributes and child entities

We do not create a separate class for each entity type, instead we use a single Entity class
and parse the XML. Based on the type of the entity and its associated spec, we populate the
attributes and child entities.

'''

spec = init_spec()

class Entity:
    def __init__(self, element):
        self.element = element
        self.parse()

    def tag(self):
        return self.element.tag
    
    def parse(self):
        if self.element.tag in spec:
            _map = spec[self.element.tag]["map"]
            required = spec[self.element.tag]["required"]
            ctags = spec[self.element.tag]["ctags"]

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

def main():
    archive = zipfile.ZipFile(sys.stdin.buffer, 'r')

    file_names = archive.namelist()
    taskdata_file_name = next((f for f in file_names if f.endswith('TASKDATA.XML')), None)

    if taskdata_file_name is None:
        print("No TASKDATA.XML file found in archive")
        sys.exit(1)
    else:
        taskdata = archive.read(taskdata_file_name)
        root = ET.fromstring(taskdata)

        assert root.tag == "ISO11783_TaskData"

        taskdata_entity = Entity(root)

if __name__ == "__main__":
    main()