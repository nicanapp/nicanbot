from lib.navigator import Navigator
from entidades.Publish import Publish
from abc import ABC, abstractmethod

class Login(ABC):
    
    logged = False
    fail = False

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator
        self.onCreate()

    def isLogged(self) -> bool:
        return self.logged
    
    def isFail(self) -> bool:
        return self.fail

    @abstractmethod
    def onCreate(self) -> None:
        pass

    @abstractmethod
    def login(self) -> None:
        pass


class Main(ABC):

    navigator:Navigator = None

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator

    @abstractmethod
    def getPublish(self) -> Publish | list[Publish]:
        pass