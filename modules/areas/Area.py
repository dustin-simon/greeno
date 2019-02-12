from core.exception.AreaNameExistException import AreaNameExistException
from core.exception.InvalidNameException import InvalidNameException

class Area():
    areas = {}

    @staticmethod
    def getByName(name):
        if name in areas:
            return areas[name]

        raise InvalidNameException(name)

    @staticmethod
    def isValidName(name):
        if name == '' or name == None:
            return False
        
        return True

    def __init__(self, name, parent):
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
