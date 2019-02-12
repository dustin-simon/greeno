from core.config.config import Config

class AreaConfig(Config):
    
    instance = None

    def getInstance():
        if instance == None:
            instance = AreaConfig()
        
        return instance

    def __init__(self):
        pass
    