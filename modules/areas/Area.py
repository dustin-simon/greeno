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
        pass
        #TODO: init module

    @classmethod
    def getByName(name):
        if name in areas:
            return areas[name]

        raise ValueError("Area with name '" + name + "' does not exist.")

    @classmethod
    def has(name):
        return name in areas

    @classmethod
    def isValidName(name):
        if name == '' or name == None:
            return False
        
        return True

    def __init__(self, name='', parent=None):
        if not isValidName(name):
            raise ValueError("'" + name + "' is not a valid name for an area.")

        if name in areas:
            raise ValueError("An area with name '" + name + "' does already exist.")
        
        if parent == None:
            pass
            #TODO: set root area as parent
        else:
            self.parent = parent

        self.subAreas = []
        self.observers = []
