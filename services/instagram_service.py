from entidades.Service import Service
from lib.instagram import *
from lib.navigator import Navigator

SLUG_SERVICE = "instagram"

async def main(service:Service):

    navigator = Navigator("https://www.instagram.com/")
    expressao = service.getExpressao()
    hashtags  = expressao.getHashTags()

    if InstLogin(navigator).isFail():
        # erro ao tentar entrar no instagram
        # bloquear a conta 
        pass
    
    main = InstMain(navigator)
    main.checkPop()

    for tag in hashtags:

        main.setStartNext(False)
        main.pesquisa(tag)

        while True:
            pub = main.getPublish()
            if pub != False:
                expressao.addPublish(SLUG_SERVICE, pub)
            if not main.next(): break

    expressao.commitPublish(SLUG_SERVICE)

    navigator.saveState()
    navigator.sleep()