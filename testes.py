from lib.twitter import TwitterLogin, TwitterMain
from lib.navigator import Navigator

navigator = Navigator("https://twitter.com/")
TwitterLogin(navigator)