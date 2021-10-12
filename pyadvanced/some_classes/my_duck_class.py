# all classes ultimately descend from the Object type

class Duck():
    # class can have properties
    count = 0
    # class can have methods
    def how_many(clas):
        print('Duck has {} instances'.format(clas.count))
    # usually classes have __init__ method, which is optional and not a constructor though it behaves like a constructor
    def __init__(self, name):
        # self.name = name
        self.__name = name
        Duck.count += 1
    def __str__(self):
        return 'This is a Duck called {}'.format(self.__name)
    # we often use getter and setter methods to access and mutate properties
    @property
    def name (self):
        return self.__name
    @name.setter
    def name (self, new_name):
        self.__name = new_name

if __name__ == "__main__":
    d = Duck('Howard') # instance of Duck class
    print (d)
    d.how_many()
    d.name = 'changed'
    print (d)

    e = Duck('Hogwart') # instance of Duck class
    print (e)
    