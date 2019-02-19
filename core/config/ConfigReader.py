import os
import os.path
import xml.etree.ElementTree as ET

class ConfigReader():
    
    def load(self, path):

        if not os.path.isfile(path):
            raise FileNotFoundError("File '" + path + "' does not exist!")

        tree = ET.parse(path)
        root = tree.getroot()

        elements = list(root)
        properties = {}

        for elem in elements:

            if elem.get('property') == 'true':
                tag = elem.tag
                value = elem.text.strip()
                properties[tag] = value        


        return properties