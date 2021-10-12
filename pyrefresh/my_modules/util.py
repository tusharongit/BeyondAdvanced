# utility module which can then be imported to make use of functions

import datetime

# function to validate a number
def checkInt(i):
    '''
    This utility check if the value of the input is an integer
    It will return 1 if no an integer
    '''
    # check if already an integer
    if type(i) == int or type(i) == float:
        return int(i)
    else:  # exception handling
        try:  # check if this block of code succeeds
            i = int(float(i))
        except Exception as e:  # handle the exception if code in try block fails
            print('[EXCEPTION] ',e)
            i = 1
        finally:  # optional - finally block aways runs
            pass
    return i

# check if cat c exists in tuple t, if not return default d
def checkCat(c, d, t):
    if c in t:
        return c
    fout = open('review2exc.txt','a')  # opens a file for overwriting and names the file access object as fout
    print (datetime.datetime.now(),file=fout)
    print ('[EXCEPTION] Invalid category \'{}\'. Defaulting to \'{}\''.format(c, d),file=fout)
    fout.close()

    return d


if __name__ == '__main__':
    
    #print(checkInt(3))
    #print(checkInt('asdfg'))

    allItem = ('users', 'posts', 'albums', 'photos')
    defItem = 'users'
    print(checkCat('album', defItem, allItem))

