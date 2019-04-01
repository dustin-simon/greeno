from abc import ABC

class Installable(ABC):

    @classmethod
    def setInstallationPath(self, installationPath):
        self.installationPath = installationPath