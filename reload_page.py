import threading
import requests as r
import sys

URL = 'http://ctf.slothparadise.com/about.php'

class myThread(threading.Thread):
    def __init__(self, ID, name, count):
        threading.Thread.__init__(self)
        self.threadID = ID
        self.name = name
        self.counter = count

    def run(self):
        get = r.get(URL)
        print(str(i) + ' Reloads')
        if 'KEY' in get.text:
            print(get.text)
            sys.exit(0)

for i in range(1000):
    thread = myThread(i, "Thread " + str(i), i)
    thread.start()
    thread.join()