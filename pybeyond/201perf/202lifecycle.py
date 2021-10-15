import threading
import datetime
import time
import random

def threadWorker():
    print('Thread is running')
    time.sleep(2)
    print('Thread is terminating')

def executeThread(i):
    print('{} Start thread {}'.format(datetime.datetime.now().strftime("%H:%M:%S"),i))
    sleepTime = random.randint(1,5)
    time.sleep(sleepTime)
    print('{} Join thread {}'.format(datetime.datetime.now().strftime("%H:%M:%S"),i))

if __name__ == '__main__':
    #myThread = threading.Thread(target=threadWorker) # Thread is an thread-access object, way of accessing a thread
    #myThread.start() # start running the thread
    #myThread.join() # optional, joins/comes back to main

    # run several threads at once
    for i in range(10):
        # pass arguments as a tuple to the method
        thread = threading.Thread(target=executeThread, args=(i,))
        thread.start()
        #print('Active threads: {}'.format(threading.enumerate()))
        #thread.join() # joining threads here mean they remain sequential ie not multi-threaded
    thread.join() # joining threads here mean they run in parallel ie multi-threaded

