from lib.navigator import Navigator

navigator=Navigator("https://instagram.com")

inputEmail=navigator.findElement("name", "username")
inputEmail.click()

navigator.sleep()