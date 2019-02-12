from abc import abstractmethod

class Config():

    @abstractmethod
    def load():
        pass