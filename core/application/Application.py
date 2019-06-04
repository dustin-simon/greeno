from ctypes import cdll, byref, create_string_buffer
from core.config.Config import Config
from core.application.AppConfigReader import AppConfigReader
from modules.Module import Module
from core.application.SystemStatusObserver import SystemStatusObserver


class Application():

    app = None

    STATUS_POWEROFF = 'POWEROFF'
    STATUS_REBOOT = 'REBOOT'
    STATUS_RUNNING = 'RUNNING'
    STATUS_APPLICATION_STOP = 'APPLICATION_STOP'
    STATUS_APPLICATION_RELOAD = 'APPLICATION_RELOAD'

    @staticmethod
    def getApplication():

        if Application.app == None:
            Application.app = Application()

        return Application.app
    
    def __init__(self):
        self._createConfig()
        self.status = Application.STATUS_RUNNING
        self.systemStatusObserver = SystemStatusObserver(self)

    def start(self):
        self._setProcessName()
        self.systemStatusObserver.start()
        Module.loadModules()
        #TODO: start the application

    def stop(self):
        Module.stopModules()
        print("GoodBye!")
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

    def setSystemStatus(self, newStatus, globalUpdate):
        self.status = newStatus.upper()

        if globalUpdate == True:
            statusFilePath = self.config.get("applicationPath") + "/../SYSTEM_STATUS"
            statusFile = open(statusFilePath, 'w')
            statusFile.write(newStatus.upper())
            statusFile.close()

    def getSystemStatus(self):
        return self.status

    def getSystemStatusObserver(self):
        return self.systemStatusObserver