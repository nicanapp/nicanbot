from lib.navigator import Navigator
from entidades.PublishSM import PublishSM


class InstLogin:

    navigator:Navigator = None

    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator

    def isLogged(self) -> bool:
        return True



class InstMain:

    navigator:Navigator = None
    btnNext = None


    def __init__(self, navigator:Navigator) -> None:
        self.navigator = navigator
        pop = navigator.findElement("button", "Agora não", limit=3)
        if pop != False: pop.click()


    def pesquisa(self, value:str) -> bool:
        # se encontrou alguma hashtag com o valor da pesquisa clica e retorna true
        # se não retorna false
        self.navigator.findElement("text", "Pesquisa").click()

        inputPesquisar=self.navigator.findElement("placeholder", "Pesquisar")
        inputPesquisar.click()
        inputPesquisar.value(value)

        self.navigator.sleep(1)

        if  not self.navigator.checkElement("text", "#flaviodino"):
            return False 
        
        self.navigator.findElement("text", "#flaviodino").click()    
        
        primeiraPub = self.navigator.findElement("xpath", '//*/article/div/div/div/div[1]/div[1]/a', limit=10)

        if primeiraPub != False: 
            primeiraPub.click()
            return True

        return False
    
    
    def analise(self, cliente_id:int, expressao_id:int) -> PublishSM:
        els = self.navigator.findElements("tag", "article")
        print(els[1].getText())  

    
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
