# declare a Point class which takes x and y
# no need to write get/set for x or for y
# instead, write a READ ONLY property called r
# r = (x*x + y*y)**0.5

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y # we are allowing direct acess to x and y
    # declare a read-only method called 'r' (i.e. no setter method)
    @property
    def r(self):
        r = (self.x*self.x + self.y*self.y)**0.5
        return r

if __name__ == '__main__':
    p = Point(3,4) # a 3-4-5 triangle
    print('if x is {0:.2f} and y is {1:.2f} then the hypotenuse will be {2:.2f}'.format(p.x, p.y, p.r)) # expect 5.0