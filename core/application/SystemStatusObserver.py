from threading import Thread
from core.application.Application import Application
import os, os.path

class SystemStatusObserver(Thread):

    def __init__(self, manager):
        Thread.__init__(self)
        self.systemManager = manager

    def run(self):
        from core.application.SystemManager import SystemManager

        while self.systemManager.getSystemStatus() == SystemManager.STATUS_RUNNING:
            status = self.getStatusFromFile()
            SystemManager.setSystemStatus(status.upper())

        print("goodbye!")
        sys.exit(0)

    def getStatusFromFile(self):
        systemPath = Application.getApplication().getConfig().get('applicationPath') + "/../"
        statusFile = systemPath + "SYSTEM_STATUS"

        if os.path.isfile(statusFile):
            file = open(statusFile, 'r')
            return file.readline()

        return SystemManager.STATUS_RUNNING


