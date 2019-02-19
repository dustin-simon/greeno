from core.exception.AreaNameExistException import AreaNameExistException
from core.exception.InvalidNameException import InvalidNameException
from core.application.Application import Application

class Area():
    areas = {}
    config = None

    @staticmethod
    def getByName(name):
        if name in areas:
            return areas[name]

        raise InvalidNameException(name)

    @staticmethod
    def has(name):
        return name in areas

    @staticmethod
    def isValidName(name):
        if name == '' or name == None:
            return False
        
        return True

    @staticmethod
    def _createRootArea():
        #TODO: create root area
    
    @staticmethod
    def _createConfig():
        #TODO: create area config

    def __init__(self, name, parent=None):
        if not isValidName(name):
            raise InvalidNameException(name)

        if name in areas:
            raise AreaNameExistException(name)
        
        if parent == None:
            #TODO: set root area as parent
        else:
            self.parent = parent

        self.subAreas = []
        self.observers = []
