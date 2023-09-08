from entidades.Expressao import Expressao
from entidades.ResponseServiceError import ResponseServiceError


class Service:
    
    _expressao:Expressao
    _listErrors:list[ResponseServiceError] = []

    def __init__(self, expresao:Expressao) -> None:
        self._expressao = expresao

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
 
    

