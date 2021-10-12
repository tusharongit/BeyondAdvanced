# arguments (args) and keyword arguments (kwargs) can be passed into functions

def myfn(*args):  # args is always a tuple of positional arguments
    print(args)
    for item in args:
        print(item, type(args))


def mykw(**kwargs):  # kwargs is always a dictionary of key-value arguments
    print(kwargs)

# mini-challene - add up all the positional arguments
def sumNums(*args):
    tot = 0
    for i in args:
        if type(i) == int or type(i) == float:
            tot += i
    print('total is', tot)

# build a func which takes user details e.g. username, pswd, email, age, membership, etc. and returns as a dictionary
def makeUser(**kwargs):
    return kwargs

# modular syntax
if __name__ == '__main__':  # if this is the main module, then run the following code block
    #print('main')

    #myfn(1,2,3,4,5)
    #mykw(x=1, y=2, z=True, wibble='wobble')

    #myfn(42, 'Freda')
    t = ('coffee', True, 42)
    myfn(t) # we can pass in a tuple
    #myfn(*t) # but we must unpack it

    #d = {'f':'Timnit', 'l':'Gebru'}
    #mykw(**d)

    #sumNums(1,2,3,4,5)
    #sumNums(1,2,3,4,5,'s','d','f',5)

    user1 = makeUser(name='Tushar', pswd='secret', age=39, email='tus@python.com')
    user2 = makeUser(name='Mak', pswd='sshh', age=35, email='mak@python.com', favpet='none')

    print(user1, user2)
