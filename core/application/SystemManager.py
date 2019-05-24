from core.application.SystemStatusObserver import SystemStatusObserver

class SystemManager():

    instance = None

    STATUS_POWEROFF = 'POWEROFF'
    STATUS_REBOOT = 'REBOOT'
    STATUS_RUNNING = 'RUNNING'
    STATUS_APPLICATION_STOP = 'APPLICATION_STOP'
    STATUS_APPLICATION_RELOAD = 'APPLICATION_RELOAD'

    @staticmethod
    def getInstance():

        if SystemManager.instance == None:
            SystemManager.instance = SystemManager()

        return SystemManager.instance

    def __init__(self):
        self.status = SystemManager.STATUS_RUNNING
        self.systemStatusObserver = SystemStatusObserver(self)

    def setSystemStatus(self, status):
        self.status = status

    def getSystemStatus(self):
        return self.status

    def poweroff(self):
        self.status = SystemManager.STATUS_POWEROFF

    def reboot(self):
        self.status = SystemManager.STATUS_REBOOT

    def stopApplication(self):
        self.status = SystemManager.STATUS_APPLICATION_STOP

    def reloadApplication(self):
        self.status = SystemManager.STATUS_APPLICATION_RELOAD

    def getSystemStatusObserver(self):
        return self.systemStatusObserver
