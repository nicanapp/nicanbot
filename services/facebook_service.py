from entidades.Service import Service 
from lib.facebook import * 
from lib.navigator import Navigator


async def main(service:Service):

    navigator = Navigator("https://www.facebook.com")
    expressao = service.getExpressao()

    if FacebookLogin(navigator=navigator).isFail():
        pass 

    main = FacebookMain(navigator)
    
    