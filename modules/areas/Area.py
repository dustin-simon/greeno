from core.application.Application import Application
from modules.Module import Module
from core.config.Config import Config

class Area(Module):
    areas = {}

    @classmethod
    def loadConfig(self):
        app = Application.getApplication()
        return Config(app.getConfig().get("applicationPath") + "/modules/areas/area.xml")

    @classmethod
    def loadData(self):
        pass
        #TODO: load saved data

    @classmethod
    def saveData(self):
        pass
        #TODO: save configured data

    @classmethod
    def initModule(self):
        Area(self.config.get("rootAreaName"))

    @classmethod
    def getByName(self, name):
        if name in self.areas:
            return self.areas[name]

        raise ValueError("Area with name '" + name + "' does not exist.")

    @classmethod
    def add(self, area):
        self.areas[area.getName()] = area

    @classmethod
    def has(self, name):
        return name in self.areas

    @classmethod
    def isValidName(self, name):
        if name == '' or name == None:
            return False
        
        return True

    def __init__(self, name='', parent=None):
        if not Area.isValidName(name):
            raise ValueError("'" + name + "' is not a valid name for an area.")

        if name in Area.areas:
            raise ValueError("An area with name '" + name + "' does already exist.")
        
        rootAreaName = Area.config.get("rootAreaName")

        if parent == None:
            
            if name == rootAreaName:
                self.parent = None
                print("created root area")
            else:
                self.parent = Area.getByName(rootAreaName)
                self.parent.addChild(self)
                print("created area. Parent: " + self.parent.getName())

        else:
            self.parent = parent
            self.parent.addChild(self)
            print("created area. Parent: " + self.parent.getName())

        self.name = name

        Area.add(self)

        self.subAreas = []
        self.observers = []

    def getSubAreas(self):
        return self.subAreas

    def getName(self):
        return self.name

    def addChild(self, area):
        self.subAreas.append(area)