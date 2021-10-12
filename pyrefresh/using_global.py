# global scope

g = 'global namespace'

def someFn():
    print('in the function')
    #g = 'local'
    #print(g)
    global g
    g = 'changed global g'
    print(g)

if __name__ == '__main__':
    print('in main')
    print(g)
    someFn()
    print('in main')
    print(g)
