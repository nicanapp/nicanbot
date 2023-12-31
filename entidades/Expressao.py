from entidades.Publish import Publish
from entidades.Midia import Midia
import datetime

class Expressao:

    _hashtags:list = []

    _client_id:int
    _expressao:str 
    _expressao_id:int
    _objeto_avaliacao:str
    _silencioso:bool
    _data_last_pub:datetime.date
    _midias: dict[str, Midia] = {}

    def __init__(self, client_id:int, expressao_id:int, expressao:str, objeto_avaliacao:str, silencioso=False) -> None:
        self._client_id = client_id
        self._expressao = expressao
        self._expressao_id = expressao_id
        self._objeto_avaliacao = objeto_avaliacao
        self._silencioso = silencioso

    def addHashTag(self, hashTag:str):
        self._hashtags.append(hashTag)

    def addMidia(self, slug:str, midia:Midia):
        self._midias[slug] = midia

    def addPublish(self, slug:str, publish:Publish):
        self._midias[slug].addPublish(publish)

    def commitPublish(self, slug:str):
        self._midias[slug].commit(self._objeto_avaliacao)

    def getObjetoAvaliacao(self):
        return self._objeto_avaliacao

    def getHashTags(self):
        return self._hashtags

    def getMidia(self, slug:str):
        return self._midias[slug]
    
    def getExpressao(self):
        return self._expressao
    

class ExpressaoFactory:

    def __init__(self) -> None:
        pass

    def generateByMap(client_id:int, expressao_map:{}) -> Expressao:
        expressao = Expressao(
            client_id=client_id,
            expressao_id=expressao_map["id"],
            expressao=expressao_map["expressao"],
            objeto_avaliacao=expressao_map["objeto_avaliacao"],
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