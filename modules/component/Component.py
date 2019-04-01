from abc import abstractmethod
from abc import ABC
from modules.Module import Module
from modules.component.ComponentMeta import ComponentMeta
from core.config.Config import Config


class Component(ABC, Module):

    @abstractmethod
    @classmethod
    def loadConfig(self):
        return Config(self.installationPath + "/component.xml")

    @abstractmethod
    @classmethod
    def loadData(self):
        pass
        
    @abstractmethod
    @classmethod
    def saveData(self):
        pass

    @classmethod
    def initModule(self):
        self.meta = self._createMeta()

    @classmethod
    def _createMeta(self):
        return ComponentMeta(self.installationPath + "/meta.xml")
        
    @classmethod
    def getMeta(self):
        return self.meta

    @classmethod
    def getConfig(self):
        return self.config

    @classmethod
    def setInstallationPath(self, installationPath):
        self.installationPath = installationPath

    