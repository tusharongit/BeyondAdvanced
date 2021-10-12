# python uses class-based coding
# everything in Python is an object, even a class

import datetime
import my_modules.util as u

class Thing():  # best practice to capitalize first letter of a class
    pass

class Person():
    '''
    Docstring for a class that explains the properties of a person
    such as name (string), age (positive int), email (string), etc.
    and encapsulating functions/methods to print person details, etc.
    '''
    def __init__(self, name, age, email, doj, access_lvl):  # optional constructor, runs automatically when class is instantiated, must contain self
        #print('Person initiated')
        self.__name = name
        self.__age = age
        self.__email = email
        self.__doj = doj
        self.access_lvl = access_lvl  # this invokes the access_lvl setter method, not provides direct access

    def showDetail(self):  # must contain self
        print(self)


    def getName(self):
        return self.__name

    def setName(self, newName):
        if isinstance(newName, str) and len(newName) > 0:
            self.__name = newName
        else:
            pass


    def getAge(self):
        return self.__age

    def setAge(self, newAge):
        #self.age = u.checkInt(newAge)
        if isinstance(newAge, int) and newAge > 0:
            self.__age = newAge
        else:
            pass


    def getEmail(self):
        return self.__email

    def setEmail(self, newEmail):
        if isinstance(newEmail, str) and len(newEmail) > 0 and newEmail.find('@') and newEmail.find('.', newEmail.find('@')) > 1:
            self.__email = newEmail
        else:
            pass


    @property  # declaring a property now (using decorators)
    def emailer(self):
        return self.__email

    @emailer.setter  # behaves as if email is a directly accessible/ mutable property, but internally calls the property defined above
    def emailer(self, newEmail):
        if isinstance(newEmail, str) and len(newEmail) > 0 and newEmail.find('@') and newEmail.find('.', newEmail.find('@')) > 1:
            self.__email = newEmail
        else:
            pass


    @property  # declaring a property now (using decorators)
    def doj(self):
        return self.__doj


    @property  # declaring a property now (using decorators)
    def access_lvl(self):
        return self.__access_lvl

    @access_lvl.setter  # behaves as if email is a directly accessible/ mutable property, but internally calls the property defined above
    def access_lvl(self, newLvl):
        levels_t = ('guest', 'user', 'admin', 'super')
        if newLvl in levels_t:
            self.__access_lvl = newLvl
        else:
            self.__access_lvl = 'guest'

    def __str__(self):  # can be used to control how print behaves for objects of this class
        newPrint = 'Name: {} Age: {} Access: {}\n'.format(self.__name, self.__age, self.__access_lvl)
        newPrint += 'Email: {} Joined: {}'.format(self.__email, self.__doj.strftime('%A %d %b %Y'))
        return newPrint

def prettyDate():
    pass

if __name__ == '__main__':
    t = Thing()  # instantiate a class
    p = Person('Tushar', 39, 'tushar@email.com', datetime.datetime.today(), 'admin')
    # print(p.__name, p.__age, p.__email)  # fails as __name, etc. is not accessible directly
    #print(p.access_lvl)
    #print(p.showDetail())
    #p.setName('Mathur')
    #p.getName()
    #p.setAge(40)
    #p.getAge()
    #p.setEmail('Mathur@email.com')
    #p.getEmail()
    #p.access_lvl = 'super'
    #print(p.showDetail())
    #print(p.access_lvl)
    #p.access_lvl = 'root'
    #print(p.showDetail())
    #print(p.access_lvl)
    print(p)
