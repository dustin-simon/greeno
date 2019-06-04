from abc import abstractmethod
from abc import ABC
from core.config.Config import Config
from modules.ModuleConfigReader import ModuleConfigReader
import importlib
import string
import random
import hashlib
import os
import os.path

class Module(ABC):

    modules = []

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
            moduleClass.startModule(name)

            self.modules.append(moduleClass)

    @classmethod
    def _createGlobalConfig(self):
        from core.application.Application import Application
        confPath = Application.getApplication().getConfig().get("applicationPath") + "/config/modules/modules.xml"
        self.moduleConf = Config(confPath, ModuleConfigReader())
        self.moduleConf.load()

    @classmethod
    def stopModules(self):
        for m in self.modules:
            m.closeModule()

    @classmethod
    def getModuleName(self):
        return self.name
 
    @classmethod
    def startModule(self, name):
        self.name = name
        self.config = self.loadConfig()
        self.config.load()
        self.prepareSavePath()
        self.initModule()
        self.loadData()

    @classmethod
    def getConfig(self):
        return self.config

    @classmethod
    def prepareSavePath(self):
        from core.application.Application import Application
        appSavePath = Application.getApplication().getConfig().get("savePath")

        savePath = appSavePath + "/" + self.name

        self.config.getProperties()["savePath"] = savePath

        if not os.path.isdir(savePath):
            os.makedirs(savePath)

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
    