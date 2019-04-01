from abc import ABC
from abc import abstractmethod
from modules.Module import Module
from modules.Installable import Installable
from core.config.Config import Config

class Connection(ABC, Module, Installable):

    @classmethod
    def loadConfig(self):
        return Config(self.installationPath + "/connection.xml")

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

    