from threading import Thread
import os, os.path
import sys

class SystemStatusObserver(Thread):

    def __init__(self, application):
        Thread.__init__(self)
        self.app = application

    def run(self):
        from core.application.Application import Application

        while self.app.getSystemStatus() == Application.STATUS_RUNNING:
            status = self.getStatusFromFile()
            self.app.setSystemStatus(status.upper(), False)

        Application.getApplication().stop()
        sys.exit(0)

    def getStatusFromFile(self):
        from core.application.Application import Application

        systemPath = Application.getApplication().getConfig().get('applicationPath') + "/../"
        statusFile = systemPath + "SYSTEM_STATUS"

        if os.path.isfile(statusFile):
            file = open(statusFile, 'r')
            newStatus = file.readline()
            file.close()

            newStatus = newStatus.strip()

            if newStatus != '':
                return newStatus

        return Application.STATUS_RUNNING


