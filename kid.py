import requests as r
import sys
import threading

url = 'http://ctf.slothparadise.com/about.php'

def reload_url():
    for i in range(1000):
        get = r.get(url)
        threading.Thread(target=reload_url) #To speed up the proccess
        print(str(i) + ' Reloads')
        if 'KEY' in get.text:
            print(get.text)
            sys.exit(0)
reload_url()