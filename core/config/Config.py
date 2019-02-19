import os.path
from core.config.ConfigReader import ConfigReader

class Config():

    def __init__(self, path, reader=None, extend=False):

        if path == None:
            raise ValueError("No file path given.")

        self.extendReader = None

        if reader == None:
            self.reader = ConfigReader()
        elif extend == False:
            self.reader = reader
        else:
            self.reader = ConfigReader()
            self.extendReader = reader


        self.path = path
        self.loaded = False


    def load(self):

        self.properties = self.reader.load(self.path)

        if self.extendReader != None:
            props = self.extendReader.load(self.path)
            self.properties.update(props)

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
        