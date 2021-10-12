# The Command Pattern
#
# an Agent will buy or sell stock for a client

from abc import ABCMeta, abstractmethod

# an abstract class
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade():
    def buy(self):
        print('Buy stock')

    def sell(self):
        print('Sell stock')

class Agent():
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() # can be called on demand

# concrete classes derived from abstract class Order
class BuyStock(Order):
    def __init__(self,stock):
        self.stock = stock

    def execute(self):
        return self.stock.buy()

# concrete classes derived from abstract class Order
class SellStock(Order):
    def __init__(self,stock):
        self.stock = stock

    def execute(self):
        return self.stock.sell()

if __name__ == '__main__':
    # client
    stock = StockTrade()
    buy = BuyStock(stock)
    sell = SellStock(stock)

    # invoker for the client
    agent = Agent()
    # now invoke the commands to buy or sell
    agent.placeOrder(buy)
    agent.placeOrder(sell)
