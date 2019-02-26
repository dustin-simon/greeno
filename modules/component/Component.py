from abc import abstractmethod
from abc import ABC
from modules.Module import Module

class Component(ABC, Module):

    @abstractmethod
    @classmethod
    def loadConfig(self):
        pass

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
        pass
        #TODO: init component class