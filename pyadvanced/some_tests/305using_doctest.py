import doctest

def nthpower(d,p):
    '''
    This returns a num raised to a power
    >>> nthpower(-3,2)
    9
    '''
    return d**p

def cubeIt(a,b):
    '''
    This returns a cube of all nums between a and b
    >>> cubeIt(1,3)
    [1, 8, 27]
    '''
    answers = []
    for i in range(a, b+1):
        answers.append(i*i*i)
    return answers

if __name__ == '__main__':
    print(nthpower(2,3))
    doctest.testmod(verbose=True)