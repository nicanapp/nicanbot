import requests as request
import json

headers = {
    "Authorization":"Bearer TOKEN",
    "Content-Type":"application/json"
}

req = request.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps({
    "model":"gpt-3.5-turbo",
    "messages":[
        {
            "role":"user",
            "content":"Como é o cálculo da cobra?"
        }
    ]
}))
print(req.text)