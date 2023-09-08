from entidades.Publish import Publish
from lib.analise import analiseAndCommit
import datetime

class MidiaConfig:

    _views:int = 0
    _curtidas:int = 0
    _verificados:bool = False
    _noConfig:bool

    def __init__(self, config={}) -> None:
        self._noConfig = config['noConfig']
        self._curtidas = config['curtidas']
        self._verificados = config['verificados']
        self._views = config['views']

    def compare(self, publish:Publish) -> bool:
        if self._noConfig: return True
        # compara os valores da publicação com os do config
        return True
        

class Midia:

    _midiaConfig:MidiaConfig
    _listPublish:list[Publish] = []

    def __init__(self, midiaConfig:MidiaConfig, data_last_pub:str="") -> None:
        self._midiaConfig = midiaConfig
        if not data_last_pub == "":
            datasplit = data_last_pub.split("-")
            self._data_last_pub = datetime.date(year=datasplit[0], month=datasplit[1], day=datasplit[2])

    def addPublish(self, publish:Publish):
        # verifica se a publicação dentro do padrão da MidiaConfig
        if self._midiaConfig.compare(publish):
            self._listPublish.append(publish)

    def commit(self, force=False):
        # envia as publicações para análise e upload
        if not force and len(self._listPublish < 100): return
        analiseAndCommit(self._listPublish)
        

