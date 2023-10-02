from lib.navigator import Navigator
from entidades.Publish import Publish
from entidades.Engajamento import Engajamento
from lib.config import Config
import re

# sem, min, d, h
# fazer o calculo de quantidade de dias atrás e salvar
# testar o midia config verificando se é adicionado a publicação com as config

def generatePublish(text:str, link:str) -> Publish: 
    tex = text.split("Ver tradução")[0]
    res = re.search("([\d.]+)\s*(curtidas)", tex)
    print(tex)
    eng = Engajamento()
    eng.curtidas = 0 if res == None else int(res.group(1).replace(".", ""))
    pub = Publish(midiaSlug="instagram", text=tex, link=link)
    pub.setEngajamento(eng)
    return pub
    #print(pub)


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
    startNext = False

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator
        pop = navigator.findElement("button", "Agora não", limit=3)
        if pop != False: pop.click() 

    def setStartNext(self, status:bool):
        self.startNext = status

    def pesquisa(self, hashTag:str) -> bool:

        self.navigator.goto(f"explore/tags/{hashTag}/")
        
        primeiraPub = self.navigator.findElement("xpath", '//*/article/div/div/div/div[1]/div[1]/a', 5)

        if primeiraPub != False: 
            primeiraPub.click()
            return True

        return False
    
    def getPublish(self) -> Publish:
        self.navigator.sleep(1)
        els = self.navigator.findElements("tag", "article")
        try :
            return generatePublish(els[1].getText(), self.navigator.currentUrl())
        except:
            return None
    
    def next(self) -> None:
        try :
            btns = self.navigator.findElements("css", "button>div>span", limit=3)
            if btns == False: return False
            c = len(btns)
            if c == 0 or (self.startNext and c < 2): return False
            self.startNext = True
            btns[c - 1].click()
            return True
        except:
            return False
