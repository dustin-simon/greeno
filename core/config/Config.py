import os.path
from core.config.ConfigReader import ConfigReader

class Config():

    def __init__(self, path, reader=None):

        if path == None:
            raise ValueError("No file path given.")

        if reader == None:
            self.reader = ConfigReader()
        else:
            self.reader = reader

        self.path = path
        self.loaded = False

    def load(self):

        self.properties = self.reader.load(self.path)
        self.loaded = True

    def print(self):
        for key, value in self.properties.items():
            print(key + ": " + value)

    def get(self, propertyname):

        if self.loaded != True:
            raise RuntimeError("You must load the configuration first.")

        if propertyname in self.properties:
            return self.properties[propertyname]
        else:
            raise ValueError("Property '" + propertyname + "' not available.")
            

    def getProperties(self):
        if self.loaded != True:
            raise RuntimeError("You must load the configuration first.")

        return self.properties
        