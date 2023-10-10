from entidades.Publish import Publish
from entidades.Engajamento import Engajamento
from entidades.ServiceAbstract import Login, Main
from lib.navigator import Navigator
from lib.config import Config
from datetime import date
import re

# regex que separa valores do link
# (https?:\/\/)?(www.)?(x.com\/|twitter.com\/)?([^\/]+)\/status\/([^\/]+)

# regex pega a data
# ((\d+)([\s\w]+)?(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)([^\d]+)?(\d+)?|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)([\s]+)?(\d+)([^\d]+)?(\d+)?)

def generateData(data:str):

    r = re.search("((\d+)([\s\w]+)?(jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)([^\d]+)?(\d+)?|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)([\s]+)?(\d+)([^\d]+)?(\d+)?)", data)
    if r == None: return date.today().strftime('%Y-%m-%d')
        
    maparegex = {
        1:'dia',
        8:'dia',
        3:'mes',
        6:'mes',
        5:'ano',
        10:'ano'
    }

    mapameses = {
        'Jan':'01','jan':'01','Feb':'02','fev':'02','Mar':'03','mar':'03',
        'Apr':'04','abr':'04','May':'05','mai':'05','Jun':'06','jun':'06',
        'Jul':'07','jul':'07','Aug':'08','ago':'08','Sep':'09','set':'09',
        'Oct':'10','out':'10','Nov':'11','nov':'11','Dec':'12','Dez':'12'
    }

    pmap = []

    mapa = {
        'dia':'',
        'mes':'',
        'ano':''
    }

    for key in maparegex:
        if maparegex[key] in pmap: continue
        if r.group(key+1) != None:
            pmap.append(maparegex[key])
            mapa[maparegex[key]] = r.group(key+1)

    return (mapa['ano'] if mapa['ano'] != '' else str(date.today().year))+"-"+mapameses[mapa['mes']]+"-"+(mapa['dia'] if len(mapa['dia']) < 2 else "0"+mapa['dia'])



def _generate_publish(text:str, link:str) -> Publish:

    parts = text.split("\n")
    
    # 0 - nome
    # 1 - slug @
    # 3 - data

    # len - 1 = views
    # len - 2 = curtidas
    # len - 3 = compartilhamento

    pub = Publish("twitter", text, link)
    pub.setData(generateData(parts[3]))
    
    eng = Engajamento()
    eng.visualizacoes = parts[-1]
    eng.curtidas = parts[-2]
    eng.compartilhamento = parts[-3]
    
    pub.setEngajamento(eng)

    return pub


def _get_all_publish(navigator:Navigator) -> list[Publish]:
    
    lista = []
    els = navigator.findElements('tag', 'article', 2)
    
    if els != False:
        for el in els:
            tagAs = navigator.findElements('tag', 'a', element=el)
            link = tagAs[3].getValueOf('href')
            lista.append(_generate_publish(el.getText(), link))

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

    def checkreload(self) -> None:
        btns_retry = self.navigator.findElements("text", "Retry")
        if btns_retry != False:
            for btnr in btns_retry:
                try:
                    btnr.click()
                except:
                    pass
        btns_rload = self.navigator.findElements("text", "Reload")
        if btns_rload != False:
            for btnr in btns_rload:
                try:
                    btnr.click()
                except:
                    pass           
            
    def search(self, expressao) -> None:
        self.navigator.goto(expressao)
        self.navigator.sleep(1)

    def getPublish(self) -> Publish | list[Publish]:
        return _get_all_publish(self.navigator)