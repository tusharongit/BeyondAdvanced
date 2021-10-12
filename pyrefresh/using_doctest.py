# doctest is used for unit testing a module

import doctest

def sqrt(x):
    '''
    This function returns the square root of a number
    >>> sqrt(64)
    8.0
    >>> sqrt(100)
    10.0
    '''
    return x**0.5

def cube(x):
    '''
    This function returns the cube of a number
    >>> cube(3)
    27
    >>> cube(-3)
    -27
    '''
    return x*x*x


if __name__ == '__main__':
    c = cube(8)
    print (c)

    # invoke doctest
    # doctest.testmod()  # doesn't show success
    doctest.testmod(verbose=True)