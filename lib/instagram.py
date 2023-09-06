from lib.navigator import Navigator
from entidades.Publish import Publish
from entidades.Expressao import Expressao
from lib.config import Config

class InstLogin:

    navigator:Navigator = None
    logged = True
    fail = False

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator
        inputEmail= self.navigator.findElement("name", "username", 5)
        if inputEmail != False:
            self.logged = False
            self.login()
        else:
            self.navigator.sleep(1)
            self.navigator.saveState()

    def isLogged(self) -> bool:
        return self.logged
    
    def isFail(self) -> bool:
        return self.fail
    
    def login(self):
        if self.logged: return
        try:
            inputEmail = self.navigator.findElement("name", "username",1)

            c = Config().getMap()["accounts"]["instagram"]

            inputEmail.click()
            inputEmail.value(c["user"])

            inputSenha = self.navigator.findElement("name", "password", 1)

            inputSenha.click()
            inputSenha.value(c["pass"]) 

            self.navigator.findElement("text", "Entrar", 3).click()
            self.navigator.sleep(10)
            self.navigator.saveState()
            self.logged = True
        except:
            self.fail = True


class InstMain:

    navigator:Navigator = None
    btnNext = None

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator
        pop = navigator.findElement("button", "Agora não", limit=3)
        if pop != False: pop.click() 

    def pesquisa(self, hashTag:str) -> bool:

        #self.navigator.findElement("text", "Pesquisa").click()

        #inputPesquisar=self.navigator.findElement("placeholder", "Pesquisar")
        #inputPesquisar.click()
        #inputPesquisar.value(hashTag)

        #el = self.navigator.findElement("text", hashTag, 2)

        #if el == False : 
        #    return False
        #else : el.click() 
        
        
        primeiraPub = self.navigator.findElement("xpath", '//*/article/div/div/div/div[1]/div[1]/a', 5)

        if primeiraPub != False: 
            primeiraPub.click()
            return True

        return False
    
    
    def analise(self, hashTag:str) -> Publish:
        self.navigator.sleep(1)
        els = self.navigator.findElements("tag", "article")
        try :
            els[1].getText()

        except:
            return False
    
    def next(self) -> None:
        try :
            btns = self.navigator.findElements("css", "button>div>span", limit=3)
            if btns == False: return False
            c = len(btns)
            if c == 0: return False
            btns[c - 1].click()
            return True
        except:
            return False
