# ask user to input n and print sqrt from 1 to n
# ask user to input n and check if it is a square
# use show_args to decorate each method

from my_helper import my_helper

def getAllSqrt(n):
    sqrtList = list(map(my_helper.getSqrt, range(1,n)))
    print (sqrtList)

if __name__ == '__main__':
    num = input('Enter a number (-100 to 100):')
    if isinstance(num) == 'int':
        pass
    else:
        num = 1
    getAllSqrt(int(float(num)))


    