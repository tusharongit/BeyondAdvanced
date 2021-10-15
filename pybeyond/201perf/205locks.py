import threading
import time

# global variables
count = 1
lock = threading.Lock()

def workerA():
    global count
    #lock.acquire()
    try:
        while count < 100:
            count += 1
            print('Worker A incremented count to {}'.format(count))
    except Exception as e:
        print (e)
    finally:
        #lock.release()
        pass

def workerB():
    global count
    #lock.acquire()
    try:
        while count > -100:
            count -= 1
            print('Worker B decremented count to {}'.format(count))
    except Exception as e:
        print (e)
    finally:
        #lock.release()
        pass

if __name__ == '__main__':
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print('Execution took {}secs'.format(t1-t0)) # took 0.07secs with locks, 0.3secs w/o locks