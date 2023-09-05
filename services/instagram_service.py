from entidades.ResponseService import ResponseService
from entidades.Expressao import Expressao
from lib.instagram import *
from lib.navigator import Navigator

def main(expressao:Expressao) -> ResponseService:
    navigator = Navigator("https://www.instagram.com/")

    if InstLogin(navigator).isFail():
        # erro ao tentar entrar no instagram
        # bloquear a conta 
        pass

    main = InstMain(navigator)

    main.pesquisa("#saudeebeleza")

    x = 0
    while x < 10:
        main.analise("#saudeebeleza")
        main.next()
        x += 1

    print("Encerrado")
    navigator.saveState()
    navigator.sleep()
    return ResponseService()