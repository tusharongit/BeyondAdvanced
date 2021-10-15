from threading import Thread

class MyworkerThread(Thread):
    # overwrite the default init method of Thread
    def __init__(self):
        print('Object of MyWorkerThread instantiated')
        Thread.__init__(self) # now call the init method of Thread

    # overwrite the default run method of Thread which is invoked by thread.start()
    def run(self):
        print('Thread is running')

if __name__ == '__main__':
    myThread = MyworkerThread()
    myThread.start() # invokes the run method
    myThread.join()