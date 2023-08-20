
from entidades.Engajamento import Engajamento

class PublishSM:

    expressao_id:int   = 0
    cliente_id:int     = 0
   
    rede_social_slug:str = ""
    
    avaliacao:int = 0 # 0 neutro | 1 positivo | 2 negativo

    text:str = ""
    data:str = ""
    link:str = ""

    engajamento:Engajamento = None

    def __init__(self, text, link, expressao_id, cliente_id, rede_socioal_slug) -> None:
        self.text = text
        self.link = link
        self.expressao_id = expressao_id
        self.cliente_id = cliente_id
        self.rede_socioal_slug = rede_socioal_slug
    
    def setEngajamento(self, engajamento:Engajamento) -> None:
        self.engajamento = engajamento

    def setData(self, dia, mes, ano) -> None:
        self.data = f"{ano}-{mes}-{dia}"
    
    def setAvaliacao(self, avaliacao) -> None:
        self.avaliacao = avaliacao
