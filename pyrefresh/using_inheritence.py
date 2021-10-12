# classes can inherit from other classes

from using_classes import Person

import datetime as d

# class Coder is a special type of Person
class Coder (Person):
    def __init__(self, name, age, email, doj, access_lvl, prim_lang):
        super().__init__(name, age, email, doj, access_lvl)
        self.lang = prim_lang

if __name__ == '__main__':
    c = Coder('Ada', 32, 'ada@ada.ie', d.datetime.today(), 'user', 'python')
    print(c, c.lang)
