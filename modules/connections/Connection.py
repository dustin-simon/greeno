from abc import ABC
from abc import abstractmethod
from modules.Module import Module
from modules.Installable import Installable
from core.config.Config import Config

class Connection(ABC, Module, Installable):

    connections = {}

    @classmethod
    def getByName(self, name):
        if name in self.connections:
            return self.connections[name]

        raise ValueError("Connection with name '" + name + "' not found!")

    @classmethod
    def add(self, connection):
        self.connections[connection.getname()] = connection

    @classmethod
    def has(self, name):
        return name in self.connections
 
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

    @abstractmethod
    def read(self, channel):
        pass
    
    @abstractmethod
    def write(self, channel):
        pass
