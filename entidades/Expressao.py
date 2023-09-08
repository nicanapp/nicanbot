from entidades.Publish import Publish
from entidades.Midia import Midia, MidiaConfig
import datetime

class Expressao:

    _hashtags:list = []

    _client_id:int
    _expressao:str 
    _expressao_id:int
    _objeto_analise:str
    _silencioso:bool
    _data_last_pub:datetime.date
    _midias:{} = {}

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

    def getHashTags(self):
        return self._hashtags

    def getMidia(self, slug:str):
        return self._midias[slug]
    

class ExpressaoFactory:

    def __init__(self) -> None:
        pass

    def generateByMap(client_id:int, expressao_map:{}) -> Expressao:
        expressao = Expressao(
            client_id=client_id,
            expressao_id=expressao_map["id"],
            expressao=expressao_map["expressao"],
            objeto_analise=expressao_map["objeto_analise"],
            silencioso=expressao_map["silencioso"]
        )
        for midia in expressao_map["midias"]:
            expressao.addMidia(
                slug=midia['slug'],
                midia=Midia(midia['config'])
            )
        for hashtag in expressao_map['hashtags']:
            expressao.addHashTag(hashTag=hashtag)

        return expressao