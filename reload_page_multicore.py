from multiprocessing import Process, Lock
import requests as r
import os, time, sys

URL = 'http://ctf.slothparadise.com/about.php'
lock = Lock()

class myProc(Process):
    def __init__(self, ID):
        Process.__init__(self)
        self.idx = ID

    def run(self):
        get = r.get(URL)
        #print(str(self.idx) + ' Reloads')
        if 'KEY' in get.text:
            print(get.text)
            sys.exit(0)

if __name__ == "__main__":
    start_time = time.time()
    #
    procs = list()
    for j in range(100):
        for i in range(10):
            p = myProc(i)
            procs.append(p)
            p.start()
        for proc in procs: 
            proc.join()
        time.sleep(0.1)
    #
    print("--- %s seconds ---" % (time.time() - start_time))