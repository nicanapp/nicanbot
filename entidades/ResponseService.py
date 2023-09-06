from entidades.Expressao import Expressao
from entidades.ResponseServiceError import ResponseServiceError


class ResponseService:
    
    _expressao:Expressao = None
    _listErrors:list[ResponseServiceError] = []

    def __init__(self, expressao:Expressao) -> None:
        self._expressao = expressao

    def commit(self):
        # aqui ele gera o arquivo se necessario
        # aqui ele altera o estado do script no banco de dados
        pass

    def remove(self, status=True):
        self._removeScript = status

    def success(self):
        return self._code == 1
    
    def addError(self, responseError:ResponseServiceError):
        self._listErrors.append(responseError)
        if responseError.code == 3:
            # erro critico! chama o commit
            pass

    def getExpressao(self):
        return self._expressao
    
    def setMessage(self, message:str):
        self._message = message 

    def setLocalErrorLink(self, local:str):
        self._local_error_link = local
    
    def setExpressao(self, expressao:Expressao):
        self._expressao = expressao
    

