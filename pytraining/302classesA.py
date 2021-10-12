# declare a class to represent a person

class Person(object): # first letter caps convention; 'object' is inherited by default
    # def __init__(self): # every class MUST declare function init using self; self is like this
    # def __init__(self, s): # every class MUST declare function init using self; self is like this
    def __init__(self, s, e): # every class MUST declare function init using self; self is like this
        # self.name = "Ethel"
        self._name = s
        self._email = e

    # we can declare accessor and mutator methods, like get and set
    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def setName(self, n):
        if type(n) == str and n != "":
            self._name = n
        else:
            self._name = "NA"

    def setEmail(self, e):
        self._email = e

    name = property(getName,setName)
    email = property(getEmail,setEmail)

    def showInfo(self): # every class methods MUST take self
        print("Name: {}, Email: {}".format(self._name, self._email))

class Student(Person): # class student inherits Person
    def __init__(self, nam, eml, lvl):
        super().__init__(nam, eml)
        self._level = lvl

    def getLevel(self):
        return self._level

    def setLevel(self, l):
        self._level = l

    def showInfo(self): # every class methods MUST take self
        super().showInfo()
        print("Name: {}, Email: {}, Level: {}".format(self.name, self.email, self.level))

    level = property(getLevel, setLevel)


class Coder(Person): # class student inherits Person
    def __init__(self, nam, eml, langlist):
        super().__init__(nam, eml)
        self._lang = langlist

    def getLang(self):
        return self._lang

    def setLang(self, langlist):
        self._lang = langlist

    def showInfo(self): # every class methods MUST take self
        # super().showInfo()
        print("Name: {}, Email: {}, Langs: {}".format(self.name, self.email, self.lang))

    lang = property(getLang, setLang)


# use the class classname(object):
# p = Person() # p is an instance of class Person
# p = Person("Tushar")
# p = Person ("", "tushar@mail.org")

# print(p.name, p.email)

# p.email = "tmathur@mail.org" # can be mutated

# print(p._name, p._email)

# p.showInfo()

s = Student("Charlie", "charlie@mail.org", "Class 9")
s.showInfo()

# c = Coder("Romeo", "romeo@coder.org", ["Java", "Python", "C", "C++"])
# c.showInfo()