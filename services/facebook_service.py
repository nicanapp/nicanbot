from entidades.Service import Service 
from lib.facebook import * 
from lib.navigator import Navigator

# document.querySelectorAll('div[role="feed"] > div').forEach(el => { if(el.querySelector('div[aria-label="Curtir"]') != null ) console.log(el) } )

async def main(service:Service):

    navigator = Navigator("https://www.facebook.com/")
    expressao = service.getExpressao()

    if FacebookLogin(navigator=navigator).isFail():
        pass 

    main = FacebookMain(navigator)
    main.search(expressao.getExpressao())

    i = 1
    max = 200
    while main.loadMore():
        if i > max: break
        pubs = main.getPublish()
        navigator.scrooldown()
        navigator.sleep(3)
        i+=1

    print("finalizou")
    navigator.sleep()
    
    