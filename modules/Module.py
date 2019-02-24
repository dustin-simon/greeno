from abc import abstractmethod
from abc import ABC

class Module(ABC):

    config = None
 
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

    