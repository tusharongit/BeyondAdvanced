# using re-enterant locks
import threading
import time

class MyWorker(): # not inheriting from Thread, so its not a Thread object class
    def __init__(self):
        self.a = 100
        self.b = 200
        self.rlock = threading.RLock() # re-entrant lock
    
    def modifyA(self):
        with self.rlock:
            print('RLock acquired {}, modifying A {}'.format(self.rlock._is_owned(),self.a))
            print('RLock: {}'.format(self.rlock))
            self.a += 1
            time.sleep(5)

    def modifyB(self):
        with self.rlock:
            print('RLock acquired {}, modifying B {}'.format(self.rlock._is_owned(),self.b))
            print('RLock: {}'.format(self.rlock))
            self.b -= 1
            time.sleep(2)

    def modifyBoth(self):
        with self.rlock:
            print('RLock acquired {}, modifying A {} and B {}'.format(self.rlock._is_owned(),self.a,self.b))
            self.modifyA()
            print('RLock: {}'.format(self.rlock))
            self.modifyB()
            print('RLock: {}'.format(self.rlock))
        print('RLock: {}'.format(self.rlock))

if __name__ == '__main__':
    w = MyWorker()
    w.modifyA()
    w.modifyB()
    w.modifyBoth()
