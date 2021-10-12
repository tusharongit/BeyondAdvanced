# each processor and each process can run many threads - multithreading
# all threads in a processor share a single instance of python

from threading import Thread
import time
import random
import sys

# create a thread-runnable function
def myFunc(name):
    # do a time-consuming operation
    for i in range(1,5):
        time.sleep(random.random()*0.9)
        sys.stdout.write(name+'\n')

if __name__ =='__main__':
    # call func several times so while one is sleeping, the other can execute
    thr1 = Thread(target=myFunc, args=('1',)) # args must be a tuple
    thr2 = Thread(target=myFunc, args=('22',))
    thr3 = Thread(target=myFunc, args=('333',))
    thr4 = Thread(target=myFunc, args=('4444',))

    # start any thread
    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()

    # rejoin to the main thread __main__
    thr1.join()
    thr2.join()
    thr3.join()
    thr4.join()