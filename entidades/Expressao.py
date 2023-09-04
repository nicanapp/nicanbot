
class Expressao:

    _hashtags:list = []
    _client_id:int
    _expressao:str 


    def __init__(self, client_id:int, expressao:str, data_last) -> None:
        self._client_id = client_id
        self._expressao = expressao

    def setHashTag(self, hashTag:str):
        self._hashtags.append(hashTag)