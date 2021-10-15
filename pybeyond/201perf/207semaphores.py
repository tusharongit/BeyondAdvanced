# semaphores allow multiple threads to be accessed
#
# ticket sellers, each trying to sell tickets for a single show
#
import threading
import time
import random

class TktSeller(threading.Thread):
    tktSold = 0

    def __init__(self, sem):
        threading.Thread.__init__(self)
        self.__sem = sem
        print('Ticket seller {} started selling tickets'.format(self.getName()))

    def run(self):
        global tktAvl
        running = True
        while running:
            self.randDelay()
            self.__sem.acquire() # we have access to the semaphore shared by all ticket sellers
            # stop when no tickets left
            if (tktAvl <= 0):
                running = False
            else:
                # selling tickets
                self.tktSold += 1
                tktAvl -= 1
                print('{} sold a ticket - {} remaining'.format(self.getName(), tktAvl))
            self.__sem.release()
        # when the while loop ends, we're all done
        print('Ticket seller {} sold {} tickets'.format(self.getName(), self.tktSold))

    def randDelay(self):
        time.sleep(random.randint(0,4)/4) # delay of either 0 / 0.25 / 0.5 / 0.75 secs

if __name__ == '__main__':
    tktAvl = 200
    sellers = []
    sem = threading.Semaphore(64) # optional param - how many simultaneous semaphores are allowed

    # use the semaphore in tkt seller instances
    for i in range(32): # no of ticket sellers
        seller = TktSeller(sem)
        seller.start()
        sellers.append(seller)
    for seller in sellers:
        seller.join()

