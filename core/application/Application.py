from ctypes import cdll, byref, create_string_buffer
from core.config.Config import Config
from core.application.AppConfigReader import AppConfigReader
from modules.Module import Module


class Application():

    app = None

    @staticmethod
    def getApplication():

        if Application.app == None:
            Application.app = Application()

        return Application.app
    
    def __init__(self):
        self._createConfig()

    def start(self):
        self._setProcessName()
        Module.loadModules()
        #TODO: start the application

    def stop(self):
        pass
        #TODO: stop the application

    def restart(self):
        pass
        #TODO: restart the application
        
    def _setProcessName(self):
        name = self.config.get('name')

        libc = cdll.LoadLibrary('libc.so.6')
        buff = create_string_buffer(len(name)+1)
        buff.value = bytes(name, "UTF-8")
        libc.prctl(15, byref(buff), 0, 0, 0)
        
    def _createConfig(self):
        self.configExtendReader = AppConfigReader()
        self.config = Config("application.xml", self.configExtendReader, True)

        self.config.load()


    def getConfig(self):
        return self.config