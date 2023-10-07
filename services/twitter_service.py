from entidades.Service import Service
from lib.navigator import Navigator
from lib.twitter import TwitterLogin, TwitterMain

SLUG_SERVICE = "twitter"

async def main(service:Service):

    navigator = Navigator("https://www.twitter.com/")
    expressao = service.getExpressao()

    if TwitterLogin(navigator).isFail():
        pass

    main = TwitterMain(navigator)
    main.search("search?q="+expressao.getExpressao()+"&src=typed_query")
    navigator.sleep(2)

    max = 30
    c = 1
    dontstop = True
    while dontstop:
        navigator.scrooldown()
        publis = main.getPublish()
        for pub in publis:
            print(pub)
            print(pub.toString())
            # expressao.addPublish(SLUG_SERVICE, pub)
            c+=1
            dontstop = c < max

    print(f"Total: {c}")
    navigator.sleep()
