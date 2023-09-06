from entidades.Engajamento import Engajamento

class Publish:

    type:str

    avaliacao:int = 0 # 0 neutro | 1 positivo | 2 negativo

    text:str = ""
    data:str = ""
    link:str = ""
    textoDestacado:str = ""

    engajamento:Engajamento = None

    def __init__(self, type:str, text:str, link:str) -> None:
        self.type = type
        self.text = text
        self.link = link

    def getType(self):
        return self.type

    def setEngajamento(self, engajamento:Engajamento) -> None:
        self.engajamento = engajamento
    
    def setAvaliacao(self, avaliacao) -> None:
        self.avaliacao = avaliacao

    def setData(self, dia, mes, ano) -> None:
        self.data = f"{ano}-{mes}-{dia}"

    def setTextoDestacado(self, texto:str) -> None:
        self.textoDestacado = texto