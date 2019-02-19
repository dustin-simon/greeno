from core.config.Config import Config
from core.application.AppConfigReader import AppConfigReader

class Application():

    def __init__(self):
        self._createConfig()
        
    def _createConfig(self):
        self.configExtendReader = AppConfigReader()
        self.config = Config("application.xml", self.configExtendReader, True)

        self.config.load()


    def getConfig(self):
        return self.config