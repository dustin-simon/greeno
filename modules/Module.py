from abc import abstractmethod
from abc import ABC

class Module(ABC):
 
    @staticmethod
    def startModule():
        self.loadConfig()
        self.initModule()
        self.loadData()

    @staticmethod
    def closeModule():
        self.saveData()

    @staticmethod
    @abstractmethod
    def loadConfig():
        pass

    @staticmethod
    @abstractmethod
    def loadData():
        pass

    @staticmethod
    @abstractmethod
    def saveData():
        pass

    @staticmethod
    @abstractmethod
    def initModule():
        pass

    