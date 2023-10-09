from entidades.Publish import Publish
from lib.analise import analiseAndCommit
import datetime

class MidiaConfig:

    _views:int = 0
    _curtidas:int = 0
    _noConfig:bool

    def __init__(self, config={}) -> None:
        self._noConfig    = config['noConfig']
        self._curtidas    = config['curtidas']
        self._verificados = config['verificados']
        self._views       = config['views']

    def compare(self, publish:Publish) -> bool:
        if self._noConfig: return True
        engajamento = publish.engajamento
        if engajamento.curtidas      < self._curtidas: return False 
        if engajamento.visualizacoes < self._views:    return False
        return True
        

class Midia:

    _midiaConfig:MidiaConfig
    _listPublish:list[Publish] = []
    _unique_links: list[str] = []

    def __init__(self, midiaConfig:{}, data_last_pub:str="") -> None:
        self._midiaConfig = MidiaConfig(midiaConfig)
        if not data_last_pub == "":
            datasplit = data_last_pub.split("-")
            self._data_last_pub = datetime.date(year=datasplit[0], month=datasplit[1], day=datasplit[2])

    def addPublish(self, publish:Publish):
        # verifica se a publicação dentro do padrão da MidiaConfig
        if publish.link in self._unique_links:
            return
        self._unique_links.append(publish.link)
        if self._midiaConfig.compare(publish):
            self._listPublish.append(publish)

    def commit(self, objeto_avaliacao:str):
        # envia as publicações para análise e upload
        if analiseAndCommit(self._listPublish,objeto_avaliacao) and len(self._unique_links) > 500:
            self._unique_links = []
        

