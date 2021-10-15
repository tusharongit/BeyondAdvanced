import multiprocessing

def myProcFn():
    print('Executing child process on separate processor, with its on Global Intepreter')

if __name__ == '__main__':
    print('Main process')
    myOtherProcA = multiprocessing.Process(target=myProcFn)
    myOtherProcA.start()
    myOtherProcA.join()
    myOtherProcB = multiprocessing.Process(target=myProcFn)
    myOtherProcB.start()
    myOtherProcB.join()
    myOtherProcC = multiprocessing.Process(target=myProcFn)
    myOtherProcC.start()
    myOtherProcC.join()