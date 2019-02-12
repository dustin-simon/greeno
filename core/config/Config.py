from abc import abstractmethod
from abc import ABC

class Config(ABC):

    def __init__(self, properties):
        self.properties = properties

    @abstractmethod
    def load(self):
        pass

    def print(self):
        for key, value in self.properties.items():
            print(key + ": " + value)

    def get(propertyname):
        if propertyname in self.properties:
            return self.properties[propertyname]
        else:
            raise ValueError("Property '" + propertyname + "' not available.")
        