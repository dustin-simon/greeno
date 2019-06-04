from core.application.Application import Application
from modules.Module import Module
from core.config.Config import Config
import os
import os.path
import xml.etree.ElementTree as ET

class Area(Module):

    areas = {}

    @classmethod
    def loadConfig(self):
        app = Application.getApplication()
        return Config(app.getConfig().get("applicationPath") + "/config/modules/area.xml")

    @classmethod
    def loadData(self):
        saveFile = self.config.get("savePath") + "/areas.xml"

        if not os.path.isfile(saveFile):
            return

        #TODO load areas
        

    @classmethod
    def saveData(self):
        root = ET.Element("areas")

        for ID in self.areas:
            area = self.areas[ID]

            areaElement = ET.SubElement(root, "area").text = area.getName()

        ET.ElementTree(root).write(self.config.get("savePath") + "/areas.xml",  encoding="utf-8", xml_declaration=True, default_namespace=None, method="xml", short_empty_elements=True)


    @classmethod
    def initModule(self):
        pass


    @classmethod
    def getByID(self, ID):
        if ID in self.areas:
            return self.areas[ID]

        raise ValueError("Area with name '" + name + "' does not exist.")

    @classmethod
    def getRootArea(self):
        
        if self.rootArea != None:
            return self.rootArea

        return None

    @classmethod
    def add(self, area):
        self.areas[area.getID()] = area

    @classmethod
    def _setRootArea(self, area):
        self.rootArea = area

    @classmethod
    def has(self, name):
        return name in self.areas

    @classmethod
    def isValidName(self, name):
        if name == '' or name == None or name == Area.config.get("rootAreaName"):
            return False
        
        return True

    def __init__(self, name='', parent=None):
        
        if parent == None:
            
            rootAreaName = Area.config.get("rootAreaName")

            if name == rootAreaName:
                self.parent = None
                Area._setRootArea(self)
            else:
                if not Area.isValidName(name):
                    raise ValueError("'" + name + "' is not a valid name for an area.")

                self.parent = Area.getRootArea()
                self.parent.addSubArea(self)

        else:

            if parent.hasSubAreaName(name):
                raise ValueError("A subarea with name '" + name + "' does already exist in this area.")

            if not Area.isValidName(name):
                raise ValueError("'" + name + "' is not a valid name for an area.")

            self.parent = parent
            self.parent.addSubArea(self)

        self.name = name
        self.ID = Module.getUniqueID()

        self.subAreas = []
        self.observers = []

        Area.add(self)

    def getID(self):
        return self.ID

    def getObservers(self):
        return self.observers

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, attributeMeta):
        pass
        #TODO: remove observer for attribute

    def getName(self):
        return self.name

    def setName(self, newName):

        if self.parent != None and self.parent.hasSubAreaName(newName):
            raise ValueError("A subarea with name '" + newName + "' does already exist in this area.")

        self.name = newName

    def addSubArea(self, area):

        if not area in self.subAreas:
            self.subAreas.append(area)

    def removeSubArea(self, area):
        pass
        #TODO: remove sub area
    
    def getSubAreas(self):
        return self.subAreas

    def hasSubAreas(self):
        return len(self.subAreas) > 0

    def hasSubAreaName(self, name):

        name = name.lower()

        for a in self.subAreas:
            if a.getName().lower() == name:
                return True

        return False