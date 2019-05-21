from abc import ABC
from abc import abstractmethod

class ActionHandler(ABC):

    def __init__(self, actionName):
        self.action = actionName

    def getAction(self):
        return self.action

    @abstractmethod
    def handleAction(self, jsonData):
        pass