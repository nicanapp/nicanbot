from entidades.ServiceAbstract import Login, Main
from entidades.Publish import Publish
from entidades.Engajamento import Engajamento
from lib.config import Config
from lib.navigator import Element, Navigator
import re
from datetime import date, timedelta


UNIQUE_LINKS = []

multiplys = {
    "mil":1000,
    "mi":1000000
}

mapameses = {
    'janeiro':'01','fevereiro':'02','março':'03',
    'abril':'04','maio':'05','junho':'06',
    'julho':'07','agosto':'08','setembro':'09',
    'outubro':'10','novembro':'11','dezembro':'12'
}


def _transform_els_data(num:str, var:str, ano:str) -> str:

    hoje  = date.today()

    if var in ["min", "h"]:
        return str(hoje)
    
    if var == "d":
        return str(date.today() - timedelta(days=int(num)))

    dia = "0"+num if len(num) == 1 else num
    if var in mapameses.keys():
        return f"{ano}-{mapameses[var]}-{dia}"

    return str(hoje)



def _transform_data(value:str) -> str:
    
    # ((\d+)(\sde)?\s([A-z]+)(\sde\s(\d+))?) 
    # se nao entrar nesse regex, é porque é HOJE! - foda-se

    values = re.search("((\d+)(\sde)?\s([A-z]+)(\sde\s(\d+))?)", value)
    hoje = date.today()
    
    if values == None: 
        return str(hoje)

    return  _transform_els_data(values.group(2), values.group(4), values.group(6) if values.group(6) != None else hoje.year)



def _transform_in_number(value:str, ext:str) -> int:
    
    multiply = multiplys[ext] if ext != "" else 1

    parts = value.split(",")
    val = int(int(parts[0]) * multiply)
    if len(parts) == 2:
        val += int(int(parts[1])*(multiply/10))
    return val



def _get_link_and_date(navigator:Navigator, el:Element) -> list[str] | bool:

    try:

        tagAs = navigator.findElements('tag', 'a', 2, el)
       
        naopegoulink = True
        if tagAs != False:
            for taga in tagAs:
                link = taga.getValueOf('href')
                test = re.search("((https:\/\/)?(www.)?facebook.com\/[^\s]+\/videos\/[\d]+\/|(https:\/\/)?(www.)?facebook.com\/photo\/\?fbid=[\d]+)", link)
                if test != None:
                    link = test.group(1)
                    naopegoulink = False
                    break

        if naopegoulink: return False

        tagA:Element = tagAs[3] 

        span1    = navigator.findElement('tag', 'span', 2, tagA)
        span     = navigator.findElement('tag', 'span', 2, span1)
        spandata = navigator.findElement("id", span.getValueOf('aria-labelledby'))

        return [ link,  spandata.getText()]

    except:

        return False

    

def _generate_pubs(navigator:Navigator, els:list[Element]) -> list[Publish]:
    
    lista = []    

    for el in els:
        
        text = el.getText()

        if text != "":

            infos = _get_link_and_date(navigator, el)

            if not infos: continue
                #print("deve ser rels")         

            link = infos[0]

            if link not in UNIQUE_LINKS:

                UNIQUE_LINKS.append(link)

                data = _transform_data(infos[1])

                try:

                    compartilhamento_num = "0"
                    curtidas_num = "0"

                    compartilhamento_ext = ""
                    curtidas_ext = ""

                    compres = re.search("([\d,]+)(\s(mil|mi))?\scompartilhamento", text)
                    if compres != None:
                        compartilhamento_num = compres.group(1)
                        compartilhamento_ext = compres.group(3) if compres.group(3) != None else ""

                    curtires = re.search("[^\d\w_\-:\.\+\[\]\{\}\*\$\%\\\&]+([\d,]+)(\s(mil|mi))?\n", text)
                    if  curtires != None:
                        curtidas_num = curtires.group(1)
                        curtidas_ext = curtires.group(3) if curtires.group(3) != None else ""

                    compartilhamento = _transform_in_number(compartilhamento_num, compartilhamento_ext)
                    curtidas = _transform_in_number(curtidas_num, curtidas_ext)

                    conteudo = text.split("Todas as reações:")[0].split("·")[2]

                    pub = Publish("facebook", conteudo, link)
                    pub.setData(data)

                    eng = Engajamento()
                    eng.compartilhamento = compartilhamento 
                    eng.curtidas = curtidas
                    
                    pub.setEngajamento(eng)
                    
                    lista.append(pub)

                    """
                    print("=========================================================")
                    print("link: "+link)
                    print("data: "+data)
                    print(conteudo)
                    print("---------------------------------------------------------")
                    print("compartilhamento: " + str(compartilhamento))
                    print("curtidas: "+ str(curtidas))
                    print("=========================================================")
                    """
          
                except:
                    # envia erro ao servidor
                    pass

    return lista



class FacebookLogin(Login):


    inputEmail:Element | bool = False


    def onCreate(self) -> None:
        
        self.inputEmail = self.navigator.findElement('name', 'email', 5)
        self.logged = self.inputEmail == False

        if not self.logged:
            return self.login()
        
        self.fail = False    

    
    def login(self) -> None:

        conta = Config().getMap()['accounts']['facebook']
        
        self.inputEmail.click()
        self.inputEmail.value(conta['user'])

        inputpass = self.navigator.findElement('name', 'pass')
        inputpass.click()
        inputpass.value(conta['pass'])

        self.navigator.sleep(1)
        
        try: 
            self.navigator.findElement('text', 'Entrar').click()
            self.fail = False    
            self.navigator.sleep(2)
            self.navigator.saveState()
        except:
            print("erro")



class FacebookMain(Main):


    atualCount:int = 0


    def search(self, expressao:str):
        self.navigator.goto(f"search/posts?q={expressao}")
        self.navigator.sleep(3)


    def loadMore(self) -> bool:
        lastCount = self.atualCount
        self.atualCount = len(self.navigator.findElements("xpath", '//div[@role="feed"]/div'))
        return lastCount < self.atualCount


    def getPublish(self) -> Publish | list[Publish]:
        divs = self.navigator.findElements("xpath", '//div[@role="feed"]/div')
        return _generate_pubs(self.navigator, divs)
