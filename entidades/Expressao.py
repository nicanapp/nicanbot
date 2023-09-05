from entidades.Publish import Publish

class Expressao:

    _hashtags:list = []
    _listPublish:list = []
    _client_id:int
    _expressao:str 
    _expressao_id:int


    def __init__(self, client_id:int, expressao_id:int, expressao:str, data_last) -> None:
        self._client_id = client_id
        self._expressao = expressao
        self._expressao_id = expressao_id

    def setHashTag(self, hashTag:str):
        self._hashtags.append(hashTag)

    def setPublish(self, publish:Publish):
        self._listPublish.append(publish)

    def commit(self):
        # sobe todas as publicações encontradas
        pass
