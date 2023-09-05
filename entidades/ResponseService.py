
"""

codigos: 
1 -> sucesso
2 -> erro parcial  - erros que não interferem na execução do código
3 -> erro perigoso - mesmos erros ocorrendo com frequencia
4 -> erro critico  - erro que interfere na execução do código

o script pode socilitar a indisponibilidade dele por causa de determinados erros

"""


class ResponseService:
    
    _code:int = 1
    _count_errors:int = 0
    _message:str = ""
    _local_error_link:str = ""
    _script:str
    _removeScript:bool = False

    def __init__(self, script) -> None:
        self._script = script

    def commit(self):
        # aqui ele gera o arquivo se necessario
        # aqui ele altera o estado do script no banco de dados
        pass

    def remove(self, status=True):
        self._removeScript = status

    def success(self):
        return self._code == 1
    
    def addError(self):
        self._count_errors += 1

    def getCode(self):
        return self._code
    
    def getCount(self):
        return self._count_errors
    
    def setCode(self, code:int):
        self._code = code
    
    def setMessage(self, message:str):
        self._message = message 

    def setLocalErrorLink(self, local:str):
        self._local_error_link = local
    
    

