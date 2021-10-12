# mathematical operations

from modules import my_module

def getRange (start, stop, step=1):
    """
    returns the list of numbers between start and stop, with a step default to 1
    """
    result = [n for n in range(start, stop, step)]
    return result

def findMean (*args):
    """
    Mean = sum / no. of args
    """
    total = my_module.addStuff(*args)
    return total/len(args)

def powerIt (n, p):
    return n**p

def squareIt (n):
    #return n*n
    return powerIt (n,2)

def squareNums (n1, n2):
    sqNums = []
    for i in range(n1,n2):
        sqNums.append(squareIt(i))
    return sqNums



if __name__ == "__main__":
    print(findMean(1,4))
    print(squareIt(11))

