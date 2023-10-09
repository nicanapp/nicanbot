from entidades.Service import Service
from lib.navigator import Navigator
from lib.twitter import TwitterLogin, TwitterMain

SLUG_SERVICE = "twitter"

async def main(service:Service):

    navigator = Navigator("https://www.twitter.com/")
    expressao = service.getExpressao()

    if TwitterLogin(navigator).isFail():
        return

    main = TwitterMain(navigator)
    main.search("search?q="+expressao.getExpressao()+"&src=typed_query")
    navigator.sleep(5)

    max = 30
    c = 1
    dontstop = True
    while dontstop:
        main.checkreload()
        publis = main.getPublish()
        for pub in publis:
            print(pub)
            print(pub.toString())
            # expressao.addPublish(SLUG_SERVICE, pub)
            c+=1
            dontstop = c < max
        navigator.scrooldown()
        navigator.sleep(5)
    print(f"Total: {c}")
    navigator.sleep()
