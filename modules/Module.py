from abc import abstractmethod
from abc import ABC

class Module(ABC):
 
    @classmethod
    def startModule(self):
        self.loadConfig()
        self.initModule()
        self.loadData()

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

    