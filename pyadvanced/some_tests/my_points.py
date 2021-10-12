class Point():
    '''
    Class represneting a point in x-y space
    '''
    points = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.points += 1 # this is the points var in the class, not for each object

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) == int:
            self.__x = new_x
        else:
            raise TypeError

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) == int:
            self.__y = new_y
        else:
            raise TypeError
    
    def hypot (self):
        '''
        Derive the hypotenuse from x and y
        '''
        return ((self.x**2 + self.y**2) ** 0.5)
    
    def moveBy (self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def display(self):
        return (self.x, self.y)

if __name__ == '__main__':
    p1 = Point(3,4)
    print(p1.hypot())

    p2 = Point(-3,-4)
    print(p2.hypot())

    p2.moveBy(4,7)
    print(p2.display())

    print (Point.points)
