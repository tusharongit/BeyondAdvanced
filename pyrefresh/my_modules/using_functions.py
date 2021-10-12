# we can encapsulate logic in a resusable function

def doStuff():
    print('stuff is happening')

def doStuff2(val):
    print(val**2)

x = 0

while x<5:
    break
    #x += 1
    #doStuff2(x)

# find the hypotenuse of a right-angeled traingle
# def pythag(x,y):
def pythag(x=3,y=4): #default values
    '''
    This is a docstring - use this for multi-line comments for effective documentation of code

    This func takes in the two sides and returns the hypotenuse
    hypot = root of the sum of squares of the sides

    '''
    r = (x*x + y*y)**0.5
    return r

if __name__ == '__main__': # ONLY run if this is the main module; ie won't run when this py is imported
    print (pythag(3,4))
    print (pythag(30,40))
    print (pythag())  # uses default x=3, y=4
    print (pythag(3)) # uses default of y only
    print (pythag(y=4)) # uses default of x only
