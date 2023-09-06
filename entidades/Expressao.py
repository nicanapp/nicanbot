from entidades.Publish import Publish
from entidades.Midia import Midia
import datetime

class Expressao:

    _hashtags:list = []

    _client_id:int
    _expressao:str 
    _expressao_id:int
    _objeto_analise:str
    _silencioso:bool
    _data_last_pub:datetime.date
    _midias:{}

    def __init__(self, client_id:int, expressao_id:int, expressao:str, objeto_analise:str, silencioso=False) -> None:
        self._client_id = client_id
        self._expressao = expressao
        self._expressao_id = expressao_id
        self._objeto_analise = objeto_analise
        self._silencioso = silencioso

    def addHashTag(self, hashTag:str):
        self._hashtags.append(hashTag)

    def addMidia(self, slug:str, midia:Midia):
        self._midias[slug] = midia

    def addPublish(self, slug:str, publish:Publish):
        self._midias[slug].addPublish(publish)

    def getMidia(self, slug:str):
        return self._midias[slug]
    
