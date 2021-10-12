from threading import Thread
import time
import random
import sys

# create a runnable class which inherits from Thread class
class MyThreadClass(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
    #override the run method of Thread class
    def run(self):
        # do a time-consuming operation
        for i in range(1,5):
            time.sleep(random.random()*0.9)
            sys.stdout.write(self.name+'\n')        
    
if __name__ == '__main__':
    tc1 = MyThreadClass('My Thread Class 1')
    tc2 = MyThreadClass('My Thread Class 22')
    tc3 = MyThreadClass('My Thread Class 333')
    tc4 = MyThreadClass('My Thread Class 4444')

    # start threads
    tc1.start()
    tc2.start()
    tc3.start()
    tc4.start()

    # rejoin to the main thread __main__
    tc1.join()
    tc2.join()
    tc3.join()
    tc4.join()
