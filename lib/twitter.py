from entidades.Publish import Publish
from entidades.Engajamento import Engajamento
from entidades.ServiceAbstract import Login, Main
from lib.navigator import Navigator
from lib.config import Config


def _generate_publish(text:str) -> Publish:
    pub = Publish("twitter", text, "link")
    eng = Engajamento()
    pub.setEngajamento(eng)
    return pub

def _get_all_publish(navigator:Navigator) -> list[Publish]:
    lista = []
    els = navigator.findElements('tag', 'article', 2)
    if els != False:
        for el in els:
            lista.append(_generate_publish(el.getText()))
    return lista

class TwitterLogin(Login):

    entrarBtn = None

    def login(self) -> None:
        self.entrarBtn.click()
        try:
            inputemail = self.navigator.findElement('name', "text", 2)
            conta = Config().getMap()['accounts']['twitter']
            inputemail.value(conta["user"])
            self.navigator.findElement('text', "Avançar", 2).click()
            inputpass = self.navigator.findElement('name', "password", 2)
            inputpass.click()
            inputpass.value(conta["pass"])
            self.navigator.sleep(2)
            self.navigator.findElement("text", "Entrar").click()
            self.navigator.sleep(2)
            self.navigator.saveState()
        except:
            # avisar que está com problemas ao logan
            self.fail = True
            pass
        


    def onCreate(self) -> None:
        self.entrarBtn = self.navigator.findElement("text", "Entrar", 5)
        if self.entrarBtn != False:
            self.login()
        else:
            self.isLogged = True
        self.navigator.sleep(1)


class TwitterMain(Main):
    

    def search(self, expressao) -> None:
        self.navigator.goto(expressao)
        self.navigator.sleep(1)


    def getPublish(self) -> Publish | list[Publish]:
        return _get_all_publish(self.navigator)