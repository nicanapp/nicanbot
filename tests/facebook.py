from lib.navigator import Navigator

navigator = Navigator("http://127.0.0.1:5500/index.html")

id = ":r1d:"

resp = navigator.findElement("xpath", f'//span[@id="{id}"]')

print(resp)

navigator.sleep()