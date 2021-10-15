import threading
import time

def stdThread():
    print('Starting std thread')
    time.sleep(9)
    print('Completing std thread')

def daemonThread():
    while True:
        print('heartbeat...')
        time.sleep(2)

if __name__ == '__main__':
    std = threading.Thread(target=stdThread)
    dmn = threading.Thread(target=daemonThread)
    dmn.setDaemon(True) # daemon thread continues running until other threads end

    dmn.start()
    std.start()