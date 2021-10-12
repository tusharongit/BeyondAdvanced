# Stateful Design Pattern
# State
#    an interface that encapsulates the object's behaviour
# Concrete State
#    a subclass that implments the State interface
#
#
# a laptop can have states: On, Off, Sleep, Hibernate
# we can go from Off --> On
# we can go from On --> Sleep
# but not from Off --> Sleep

class CompState:
    name = 'state'
    allowed = [] # allowed values for state

    def switch (self, state):
        if state.name in self.allowed:
            print('Switching from {} to {}'.format(self.name, state.name))
            self.__class__ = state
        else:
            print('Cannot switch from {} to {}'.format(self.name, state.name))

    def __str__(self):
        return self.name

class On(CompState):
    name = 'On'
    allowed = ['Off', 'Sleep', 'Hibernate']

class Off(CompState):
    name = 'Off'
    allowed = ['On']

class Sleep(CompState):
    name = 'Sleep'
    allowed = ['On', 'Off']

class Hiber(CompState):
    name = 'Hibernate'
    allowed = ['On', 'Off']

class Computer():
    def __init__(self, comp_model):
        self.model = comp_model
        self.state = Off() # initial stae when computer starts

    def change(self, change_to):
        self.state.switch(change_to)


if __name__ == '__main__':
    comp = Computer('Laptop')
    comp.change(On)
    comp.change(Sleep)
    comp.change(Off)
    comp.change(Sleep)
    comp.change(On)
    comp.change(Hiber)
    comp.change(Sleep)
    comp.change(Off)