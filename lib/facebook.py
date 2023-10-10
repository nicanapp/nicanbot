from entidades.ServiceAbstract import Login, Main
from entidades.Publish import Publish


class FacebookLogin(Login):

    def onCreate(self) -> None:
        return super().onCreate()
    
    def login(self) -> None:
        return super().login()
    
class FacebookMain(Main):

    def getPublish(self) -> Publish | list[Publish]:
        return super().getPublish()