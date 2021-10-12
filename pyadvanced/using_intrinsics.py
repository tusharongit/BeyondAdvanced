# things built in to Python are called instrinsics

class TopLevel():
    def __init__(self):
        pass

class Derived(TopLevel):
    '''
    This class is derived from TopLevel
    and has its own __str__ method
    '''
    def __init__(self):
        super().__init__()
    def __str__(self):
        return ('Derived class instance')

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d) # invokes the __str__ of Derived class
    # we can explore the instrisic members of our instances
    print('Class name is {}'.format(Derived.__name__))
    print('Class is instantiated in module {}'.format(Derived.__module__))
    print('Class bases are {}'.format(Derived.__bases__))
    print('Class docstring is {}'.format(Derived.__doc__))
    print('Class dictionary is {}'.format(Derived.__dict__))

