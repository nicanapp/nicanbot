from entidades.ServiceAbstract import Login, Main
from entidades.Publish import Publish
from lib.config import Config
from lib.navigator import Element, Navigator
import re


UNIQUE_LINKS = []

multiplys = {
    "mil":1000,
    "mi":1000000
}


def _transform_in_number(value:str, ext:str) -> int:
    
    multiply = multiplys[ext] if ext != "" else 1

    parts = value.split(",")
    val = int(int(parts[0]) * multiply)
    if len(parts) == 2:
        val += int(int(parts[1])*(multiply/10))
    return val


def _get_link(navigator:Navigator, el:Element) -> str:

    tagAs = navigator.findElements('tag', 'a', 2, el)

    if tagAs != False:
        for taga in tagAs:
            link = taga.getValueOf('href')
            test = re.search("((https:\/\/)?(www.)?facebook.com\/[^\s]+\/videos\/[\d]+\/|(https:\/\/)?(www.)?facebook.com\/photo\/\?fbid=[\d]+)", link)
            if test != None:
                return test.group(1)

    return ""


def _generate_pubs(navigator:Navigator, els:list[Element]) -> list[Publish]:
    
    lista = []

    for el in els:
        text = el.getText()
        if text != "":
            link = _get_link(navigator, el)
            if link not in UNIQUE_LINKS:

                UNIQUE_LINKS.append(link)

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

                print("=========================================================")
                print(link)
                print(text)
                print("---------------------------------------------------------")
                print("compartilhamento: " + str(compartilhamento))
                print("curtidas: "+ str(curtidas))
                print("=========================================================")

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
