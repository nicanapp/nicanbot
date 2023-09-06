from entidades.ResponseService import ResponseService
from lib.instagram import *
from lib.navigator import Navigator

async def main(response:ResponseService):

    navigator = Navigator("https://www.instagram.com/")
    expressao = response.getExpressao()
    midia     = expressao.getMidia("instagram")

    if InstLogin(navigator).isFail():
        # erro ao tentar entrar no instagram
        # bloquear a conta 
        pass

    main = InstMain(navigator)

    main.pesquisa("#saudeebeleza")

    x = 0
    while True:
        main.analise("#saudeebeleza")
        if not main.next(): break

    navigator.saveState()
    navigator.sleep()