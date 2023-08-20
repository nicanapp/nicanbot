from lib.navigator import Navigator
from lib.instagram import InstLogin, InstMain

navigator=Navigator("https://www.instagram.com/")

login = InstLogin(navigator)

if login.isLogged(): print("Logado")

main = InstMain(navigator)
if not main.pesquisa("#flaviodino"):
    print("nao foi")

navigator.sleep(2)

i = 0
while i < 10:
    navigator.sleep(1)
    main.analise()
    main.next()
    i+=1
    
navigator.saveState()
navigator.sleep()
