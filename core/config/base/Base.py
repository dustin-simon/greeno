import os
import xml.etree.ElementTree as ET
from core.config.Config import Config

class BaseConfig(Config):

    def __init__(self):
        properties = self.load()

        super().__init__(properties)

    def load(self):
        APPLICATION_PATH = os.getcwd()

        xml_path = APPLICATION_PATH + "/application.xml"
        tree = ET.parse(xml_path)
        root = tree.getroot()

        APPLICATION_NAME = root.find('name').text
        VERSION = root.find('version').text
        LICENSE = root.find('license').text
        COPYRIGHT = root.find('copyright').text
        AUTHOR = root.find('author').text 

        properties = {
            "application path" : APPLICATION_PATH,
            "application name" : APPLICATION_NAME,
            "version" : VERSION,
            "license" : LICENSE,
            "copyright" : COPYRIGHT,
            "author" : AUTHOR 
        }

        return properties






