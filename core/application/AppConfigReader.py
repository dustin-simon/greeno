from core.config.ConfigReader import ConfigReader
import os 

class AppConfigReader(ConfigReader):

    def load(self, path):
        
        return {
            "applicationPath" : os.getcwd()
        }
