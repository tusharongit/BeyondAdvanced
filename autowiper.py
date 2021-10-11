class WiperState:
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

class Off(WiperState):
    name = 'Off'
    allowed = ['Slow']

class Slow(WiperState):
    name = 'Slow'
    allowed = ['Off','Fast']

class Fast(WiperState):
    name = 'Fast'
    allowed = ['Slow']


class Wiper():
    def __init__(self, wiper_mode):
        self.mode = wiper_mode
        print('Wipers set to {}'.format(self.mode))
        self.state = Off() # initial stae when computer starts

    def change(self, change_to):
        self.state.switch(change_to)


if __name__ == '__main__':
    comp = Wiper('Auto')
    comp.change(Slow)
    comp.change(Fast)
    comp.change(Off)
    comp.change(Slow)
    comp.change(Off)
    comp.change(Fast)
    comp.change(Slow)
    comp.change(Off)