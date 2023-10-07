from entidades.Publish import Publish
from lib.api import API
from lib.chatgpt import avaliacao

def analiseAndCommit(publicacoes:list[Publish], objeto_avaliacao:str) -> bool:
    # chatgpt analise e salva no banco de dados
    for pub in publicacoes:
        print(pub.toString())
        # avaliacao(pub, objeto_avaliacao)
    