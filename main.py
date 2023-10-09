import asyncio
from entidades.Service import Service
from entidades.Expressao import ExpressaoFactory
from services.instagram_service import main as instagram_service
from services.twitter_service import main as twitter_service
from lib.api import dummyData


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
        
        client_id = client["id"]

        for expressao_map in client["expressoes"]:
            expressao_map["client_id"] = client_id
            service = Service(
                ExpressaoFactory.generateByMap(client_id=client_id, expressao_map=expressao_map)
                ) 

            tasks = []
            
            for midia in expressao_map["midias"]:         
                #if   midia["slug"] == "instagram": tasks.append(instagram_service(service))
                if midia["slug"] == "twitter"  : tasks.append(twitter_service(service))
                #if midia["slug"] == "facebook" : tasks.append(facebook_service(service))

            await asyncio.gather(*tasks)

asyncio.run(main())

