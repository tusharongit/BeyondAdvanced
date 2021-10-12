def getSqrt(a):
    '''
    A simple method to return the square root of a number
    '''
    return a**0.5

def getSq(a):
    '''
    A simple method to return the square of a number
    '''
    return a**2

def isSq(a):
    '''
    A simple method to check if the number is a square
    '''
    sq_l= list( map(getSq, range(1,11) ) ) # take the 'square' fn and apply a bunch of numbers to it
    if a in sq_l:
        return True
    else:
        return False



if __name__ == '__main__':
    print('Square root of {} is {}'.format(9,getSqrt(9)))
    print('Square of {} is {}'.format(9,getSq(9)))
    print('{} is a square? {}'.format(80,isSq(80)))
