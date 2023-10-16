from entidades.Service import Service 
from lib.facebook import * 
from lib.navigator import Navigator

# document.querySelectorAll('div[role="feed"] > div').forEach(el => { if(el.querySelector('div[aria-label="Curtir"]') != null ) console.log(el) } )

SLUG_SERVICE = "facebook"

async def main(service:Service):

    navigator = Navigator("https://www.facebook.com/")
    expressao = service.getExpressao()

    if FacebookLogin(navigator=navigator).isFail():
        pass 

    main = FacebookMain(navigator)
    main.search(expressao.getExpressao())

    i = 1
    max = 200

    limit = 60
    stats = True
    while navigator.exec("""return document.querySelector('div[hidden="true"]').innerHTML""") == False:
        navigator.sleep(1)
        limit -= 1
        if limit == 0: stats = False

    if not stats:
        print("enviar erro ao seridor")
        return

    while main.loadMore():
        if i > max: break
        pubs = main.getPublish()
        for pub in pubs:
            expressao.addPublish(SLUG_SERVICE, pub)
        navigator.scrooldown()
        navigator.sleep(2)
        navigator.scrooldown()
        navigator.sleep(10)
        i+=1

    expressao.commitPublish(SLUG_SERVICE)
    navigator.saveState()

    print("finalizou")

    navigator.sleep()
    
    