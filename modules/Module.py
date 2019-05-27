from abc import abstractmethod
from abc import ABC
from core.config.Config import Config
from modules.ModuleConfigReader import ModuleConfigReader
import importlib
import string
import random
import hashlib

class Module(ABC):

    @staticmethod
    def getUniqueID():
        stringValue = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
        md5Value = hashlib.md5()
        md5Value.update(stringValue.encode("UTF-8"))

        return md5Value.hexdigest()

    @classmethod
    def loadModules(self):
        
        self._createGlobalConfig()
        
        for name, values in self.moduleConf.getProperties().items():
            print("module '" + name + "'")

            baseClass = values["class"]
            package = values["package"]

            moduleClass = getattr(importlib.import_module(package), baseClass)
            moduleClass.startModule()

    @classmethod
    def _createGlobalConfig(self):
        from core.application.Application import Application
        confPath = Application.getApplication().getConfig().get("applicationPath") + "/config/modules/modules.xml"
        self.moduleConf = Config(confPath, ModuleConfigReader())
        self.moduleConf.load()
 
    @classmethod
    def startModule(self):
        self.config = self.loadConfig()
        self.config.load()
        self.initModule()
        self.loadData()

    @classmethod
    def getConfig(self):
        return self.config

    @classmethod
    def closeModule(self):
        self.saveData()

    @classmethod
    @abstractmethod
    def loadConfig(self):
        pass

    @classmethod
    @abstractmethod
    def loadData(self):
        pass

    @classmethod
    @abstractmethod
    def saveData(self):
        pass

    @classmethod
    @abstractmethod
    def initModule(self):
        pass

    