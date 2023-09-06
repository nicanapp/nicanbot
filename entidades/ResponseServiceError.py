
"""

codigos: 
1 -> erro parcial  - erros que não interferem na execução do código
2 -> erro perigoso - mesmos erros ocorrendo com frequencia
3 -> erro critico  - erro que interfere na execução do código

o script pode socilitar a indisponibilidade dele por causa de determinados erros

"""

class ResponseServiceError:

    _code:int
    _remove_script:bool
    _message:str
    _local_error_link:str

    def __init__(self,message:str, link:str, code:int = 1, removeScript:bool = False) -> None:
        self.code = code
        self._message = message 
        self._local_error_link = link 
        self._remove_script = removeScript
        
    def getMessage(self):
        return self._message
    
    def getLink(self):
        return self._local_error_link