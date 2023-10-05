import requests as request
import json
from entidades.Publish import Publish
from lib.config import Config
import re


TOKEN = Config().getMap()["token_chatgpt"]

headers = {
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type":"application/json"
}


def _get_analise(message:str) -> int:
    test = re.search("(Não.+identifica)|(0)|(1)|(2)", message)
    grupos = test.groups()
    if grupos[0] != None or grupos[1] != None: return 0
    if grupos[2] != None: return 1
    if grupos[3] != None: return 2
    return 0
    

def avaliacao(publish:Publish, objeto_avaliacao:str):

    pergunta  = f"Analise a opinião/avaliação do texto abaixo sobre {objeto_avaliacao} e responda somente com 0, 1 ou 2 e nada mais."
    pergunta += "1 para positivo, 2 para negativo ou 0 se for neutro ou se não foi possivel identificar opinião/avaliação do texto. Texto: "
    pergunta += publish.text

    req = request.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps({
        "model":"gpt-3.5-turbo",
        "messages":[
            {
                "role":"user",
                "content":pergunta
            }
        ]
    }))

    if req.status_code != 200:
        return False

    resp   = json.loads(req.text)
    status = _get_analise(resp["choices"][0]["message"]["content"])
    publish.setAvaliacao(status)
    return True
