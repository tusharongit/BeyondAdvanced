# The Facade Pattern
#   hides the complexities of an internal system
#   provides an interface to the client to access the system in a simplified way
#
#                     Facade    <----   Client
#                    /  |  \
#                   /   |   \   whatever is underneath this layer is unknown to the client
#           -----------------------------------------
#                 /     |     \
#                <      V      >
#        sub-sys1   sub-sys2   sub-sys3
#
# consider skills which are sought, e.g. coder, tester, devops, designer, manager

# all classes are abstract with no inter-dependencies

class Coder():
    def __init__(self):
        print('Bring the coding skills')

    def __isAvailable__ (self):
        print('Coding skills available')
        return True

    def bookTime(self):
        if self.__isAvailable__():
            print('Coder is booked')

class Tester():
    def __init__(self):
        print('Preparing tests')

    def testing(self):
        print('Tests are in place')

class DevOps():
    def __init__(self):
        print('Networking for the team')

    def doStuff(self):
        print('Pipeline working')

class Designer():
    def __init__(self):
        print('Designing stuff')

    def makeProto(self):
        print('Wireframes and prototypes built')

class Manager(): # facade to the team members
    def __init__(self):
        print('Manager says: I can arrange the team')
    
    def arrange(self):
        # we now need instances of each uS
        self.coder = Coder()
        self.coder.bookTime()

        self.tester = Tester()
        self.tester.testing()

        self.devops = DevOps()
        self.devops.doStuff()

        self.designer = Designer()
        self.designer.makeProto()

class You(): # client to the facade
    def __init__(self):
        print('We need a team!')

    def askMgr(self):
        print('Let\'s ask the manager to arrange a team.')
        m = Manager()
        m.arrange()

    # __del__ will be called before a class closes in classic Python flavors
    # but not always in bundles like Anaconda, Jupyter
    def __del__(self):
        print('All done.')

if __name__ == '__main__':
    you = You()
    you.askMgr()

