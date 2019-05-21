from modules.Module import Module
from core.application.Application import Application
from core.config.Config import Config
import importlib
import os, os.path

class Action(Module):

    actionHandlers = {}

    @classmethod
    def getHandler(self, action):
        if action in self.actionHandlers:
            return self.actionHandlers[action]

        return None

    @classmethod
    def loadConfig(self):
        print("loading action config")
        configFile = Application.getApplication().getConfig().get('applicationPath') + "/config/modules/action.xml"
        return Config(configFile)

    @classmethod
    def loadData(self):
        print("loading actions...")
        loadPath = Application.getApplication().getConfig().get("applicationPath") + "/" + self.config.get("loadPath")
        for filename in os.listdir(loadPath):
            if os.path.isdir(loadPath + "/" + filename) and os.path.isfile(loadPath + "/" + filename + "/action.xml"):

                handler = self._createActionHandler(self.config.get("loadPath") + "/" + filename)
                self.actionHandlers[handler.getAction()] = handler

    @classmethod
    def _createActionHandler(self, path):
        fullPath = Application.getApplication().getConfig().get("applicationPath") + "/" + path
        tempConfig = Config(fullPath + "/action.xml")
        tempConfig.load()

        className = tempConfig.get("className")
        actionName = tempConfig.get("name")
        package = (path + "/" + className).replace("/", ".")
        handlerClass = getattr(importlib.import_module(package), className)

        return handlerClass(actionName)


    @classmethod
    def saveData(self):
        print("saving action data...")

    @classmethod
    def initModule(self):
        print("init actions module")