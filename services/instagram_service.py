from entidades.Service import Service
from lib.instagram import *
from lib.navigator import Navigator

async def main(service:Service):

    navigator = Navigator("https://www.instagram.com/")
    expressao = service.getExpressao()
    hashtags  = expressao.getHashTags()

    if InstLogin(navigator).isFail():
        # erro ao tentar entrar no instagram
        # bloquear a conta 
        pass
    
    main = InstMain(navigator)

    for tag in hashtags:
        main.pesquisa(tag)

        while True:
            main.analise()
            if not main.next(): break

    navigator.saveState()
    navigator.sleep()