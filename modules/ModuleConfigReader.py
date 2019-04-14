from core.config.ConfigReader import ConfigReader
import os
import os.path
import xml.etree.ElementTree as ET

class ModuleConfigReader(ConfigReader):

    def load(self, path):
        
        if not os.path.isfile(path):
            raise FileNotFoundError("File '" + path + "' does not exist!")

        tree = ET.parse(path)
        root = tree.getroot()

        modules = list(root)
        props = {}

        for module in modules:

            entries = list(module)

            name = ''
            values = {}

            for entry in entries:

                if entry.tag == 'name':
                    name = entry.text.strip()
                else:
                    values[entry.tag] = entry.text.strip()

            props[name] = values

        return props
            