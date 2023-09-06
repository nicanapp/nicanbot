
from entidades.Publish import Publish

class MidiaConfig:

    _view:int = 0
    _curtidas:int = 0
    _verificados:bool = False
    _noConfig:bool
    _slug_midia:str

    def __init__(self, slug_midia, noConfig=False) -> None:
        self._slug_midia = slug_midia
        self._noConfig = noConfig

    def setMinView(self, view:int):
        self._view = view

    def setMinCurtidas(self, curtidas:int):
        self._curtidas = curtidas

    def compare(self, publish:Publish) -> bool:
        if self._noConfig: return True
        # compara os valores da publicação com os do config
        return True
