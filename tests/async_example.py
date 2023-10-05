import asyncio
import random
from entidades.Service import Service
from lib.api import dummyData

async def instagram_service():
    for i in range(0, 10):
        await asyncio.sleep(2)
        print("instagram : "+str(i)) 

async def twitter_service():
    for i in range(0, 10):
        await asyncio.sleep(1)
        print("twitter : "+str(i)) 

async def facebook_service():
    for i in range(0, 10):
        n = random.randint(0,5)
        await asyncio.sleep(n)
        print("facebook : "+str(i)) 


"""
    1 - RECUPERA OS DOIS CLIENTES ATIVOS NO 'FULL'
    2 - RECUPERA TODOS OS OUTROS CLIENTES QUE ESTÃO SILENCIOSOS 
    3 - ANALISA OS CLIENTES SILENCIOSOS POR 3H NO MÁXIMO
    4 - ANALISA OS DOIS CLIENTES NO FULL COM AS 5 EXPRESSÕES ATIVAS DA SEGUINTE FORMA
        - VERIFICAR SE A MIDIA JA FOI ANALISADA NO DIA DE UMA EXPRESSAO (SE JA FOI A MIDIA NAO É INCLUIDA NA EXPRESSÃO)
        - CADA EXPRESSÃO SERÁ ANALISADA POR NO MÁXIMO 2H 

"""
async def main():
    
    jsonlist = dummyData()

    for client in jsonlist:
        
        print("CLIENTE ID : " + str(client["id"]))
        
        for expressao in client["expressoes"]:
            # gera o objeto Service(expressao)
            print(expressao)
            tasks = []
            
            for midia in expressao["midias"]:         
                if   midia["slug"] == "instagram": tasks.append(instagram_service())
                elif midia["slug"] == "twitter"  : tasks.append(twitter_service())
                elif midia["slug"] == "facebook" : tasks.append(facebook_service())

            await asyncio.gather(*tasks)

asyncio.run(main())


