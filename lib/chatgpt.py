import requests as request
import json
from entidades.Publish import Publish
from lib.config import Config

TOKEN = Config().getMap()["token_chatgpt"]

headers = {
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type":"application/json"
}


def avaliacao(publish:Publish, objeto_avaliacao:str):

    pergunta  = f"Analise a opinião/avaliação do texto abaixo sobre {objeto_avaliacao}."
    pergunta += "Reponda de forma curta, apenas com 0 para neutro ou se não foi possivel identificar, 1 para positivo e 2 para negativo. Texto: "
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

    publish.setAvaliacao(req.text)