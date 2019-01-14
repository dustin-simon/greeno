import os
import xml.etree.ElementTree as ET

APPLICATION_PATH = None
APPLICATION_NAME = None
VERSION = None
LICENSE = None
COPYRIGHT = None
AUTHOR = None

def initialize():
    global APPLICATION_PATH, APPLICATION_NAME, VERSION, LICENSE, COPYRIGHT, AUTHOR

    APPLICATION_PATH = os.getcwd()

    xml_path = APPLICATION_PATH + "/application.xml"
    tree = ET.parse(xml_path)
    root = tree.getroot()

    APPLICATION_NAME = root.find('name').text
    VERSION = root.find('version').text
    LICENSE = root.find('license').text
    COPYRIGHT = root.find('copyright').text
    AUTHOR = root.find('author').text
        


