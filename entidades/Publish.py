from entidades.Engajamento import Engajamento

class Publish:

    midiaSlug:str

    avaliacao:int = 0 # 0 - neutro ou não identificado | 1 - positivo | 2 - negativo

    text:str = ""
    data:str = ""
    link:str = ""
    
    engajamento:Engajamento = None

    def __init__(self, midiaSlug:str, text:str, link:str) -> None:
        self.midiaSlug = midiaSlug
        self.text = text
        self.link = link

    def getMidiaSlug(self):
        return self.midiaSlug

    def setEngajamento(self, engajamento:Engajamento) -> None:
        self.engajamento = engajamento
    
    def setAvaliacao(self, avaliacao:str) -> None:
        self.avaliacao = int(avaliacao)

    def setData(self, dia, mes, ano) -> None:
        self.data = f"{ano}-{mes}-{dia}"
