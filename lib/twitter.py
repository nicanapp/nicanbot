from entidades.Publish import Publish
from entidades.ServiceAbstract import Login, Main

class TwitterLogin(Login):

    def login(self) -> None:
        pass

    def onCreate(self) -> None:
        self.navigator.sleep()


class TwitterMain(Main):
    
    def getPublish(self) -> Publish:
        return super().getPublish()