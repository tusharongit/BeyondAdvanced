class LightsState:
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

class Off(LightsState):
    name = 'Off'
    allowed = ['On']

class On(LightsState):
    name = 'On'
    allowed = ['Off']


class Lights():
    def __init__(self, lights_mode):
        self.mode = lights_mode
        print('Lights set to {}'.format(self.mode))
        self.state = Off() # initial stae when computer starts

    def change(self, change_to):
        self.state.switch(change_to)


if __name__ == '__main__':
    comp = Lights('Auto')
    comp.change(On)
    comp.change(Off)
    comp.change(Off)
    comp.change(On)
    comp.change(On)
    comp.change(Off)