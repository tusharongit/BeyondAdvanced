#
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
        # print("inside Person showInfo")
        print("Name: {}, Email: {}".format(self._name, self._email))

class WebUser(Person): # class student inherits Person
    def __init__(self, nam, eml, lvl):
        super().__init__(nam, eml)
        self._level = lvl

    def getLevel(self):
        return self._level

    def setLevel(self, l):
        if l in ("Guest", "Admin", "Owner"):
            self._level = l
        else:
            self._level = "guest"

    def showWebUserInfo(self): # every class methods MUST take self
        # print("inside WebUser showInfo")
        # super().showInfo()
        print("Name: {}; Email: {}; Level: {}".format(self.name, self.email, self.level))

    def logWebUserInfo(self): # every class methods MUST take self
        fout = open('webusers.txt', 'wt')
        print("Name: {}; Email: {}; Level: {}".format(self.name, self.email, self.level), file=fout)
        fout.close()
    
    level = property(getLevel, setLevel)



if __name__ == "__main__":
    wu = WebUser("Charlie", "charlie@mail.org", "Admin")
    wu.showInfo()
