from abc import ABC

class Installable(ABC):

    def setInstallationPath(self, installationPath):
        self.installationPath = installationPath