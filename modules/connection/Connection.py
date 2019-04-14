import importlib
import os
import os.path
from abc import ABC
from abc import abstractmethod
from modules.Module import Module
from core.application.Application import Application
from core.config.Config import Config

class Connection(Module):

    connections = {}

    @classmethod
    def loadConfig(self):
        configFile = Application.getApplication().getConfig().get('applicationPath') + "/config/modules/connection.xml"
        return Config(configFile)

    @classmethod
    def loadData(self):
        print("loading connection data")

        loadPath = Application.getApplication().getConfig().get("applicationPath") + "/" + self.config.get("loadPath")
        for filename in os.listdir(loadPath):
            if os.path.isdir(loadPath + "/" + filename) and os.path.isfile(loadPath + "/" + filename + "/connection.xml"):

                connect = self._createConnection(self.config.get("loadPath") + "/" + filename)
                self.connections[connect.getName()] = connect
                connect.open()

    @classmethod
    def _createConnection(self, path):
        fullPath = Application.getApplication().getConfig().get("applicationPath") + "/" + path
        tempConfig = Config(fullPath + "/connection.xml")
        tempConfig.load()

        className = tempConfig.get("className")
        package = (path + "/" + className).replace("/", ".")
        print("importing " + package)
        connectionClass = getattr(importlib.import_module(package), className)

        return connectionClass(fullPath)

        

    @classmethod
    def saveData(self):
        print("saving connection data")

    @classmethod
    def getByName(self, name):
        if name in self.connections:
            return self.connections[name]

        raise ValueError("Connection with name '" + name + "' not found!")

    @classmethod
    def initModule(self):
        print("init connection module")
        self.config.print()

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def write(self, data, channel):
        pass

    @abstractmethod
    def read(self, channel):
        pass

    def __init__(self, installationPath):
        self.installationPath = installationPath
        self.config = Config(self.installationPath + "/connection.xml")
        self.config.load()
        self.config.print()

    def getName(self):
        return self.config.get("name")