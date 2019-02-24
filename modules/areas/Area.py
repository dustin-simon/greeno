from core.application.Application import Application

class Area():
    areas = {}
    config = None

    @staticmethod
    def getByName(name):
        if name in areas:
            return areas[name]

        raise ValueError("Area with name '" + name + "' does not exist.")

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

    def __init__(self, name='', parent=None):
        if not isValidName(name):
            raise ValueError("'" + name + "' is not a valid name for an area.")

        if name in areas:
            raise ValueError("An area with name '" + name + "' does already exist.")
        
        if parent == None:
            #TODO: set root area as parent
        else:
            self.parent = parent

        self.subAreas = []
        self.observers = []
