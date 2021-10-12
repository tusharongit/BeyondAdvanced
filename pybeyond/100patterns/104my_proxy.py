# The Proxy Pattern
# 'proxy' means a stand-in for other things
# Proxy class
#   acts as an interface to real objs
#   shields against malicious intentions and protects the real object
#   improve perf with caching
#
# here are some payment methods and a bank that accpets various kinds of payments

import random
from abc import ABCMeta, abstractmethod

class Payment(metaclass = ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass

class DebitCart(Payment):
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Payment proxy: Swipe, Tap or Insert Card:')
        self.bank.setCard(card)
        return self.bank.do_pay()


class Bank(Payment):
    def __init__(self):
        self.card = None
        self.acc = None

    def __getAcc (self): # private ie only avl to this class
        self.acc = self.card
        return self.acc

    def __hasFunds(self):
        print('Bank is checking if {} has sufficient funds.'.format(self.__getAcc()))
        return bool(random.getrandbits(1)) # performant way to randomly return True/False

    def setCard(self,card):
        self.card = card
    
    def do_pay(self):
        if self.__hasFunds():
            print('Bank is paying')
            return True
        else:
            print('Not sifficient funds')
            return False


class You(): # client
    def __init__(self):
        print ('I need to pay now')
        self.debitCard = DebitCart()
        self.isPurchased = None

    def makePayment(self):
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print('Purchase went smoothly')
        else:
            print('Anyone got a fiver')


if __name__ == '__main__':
    you = You()
    you.makePayment()