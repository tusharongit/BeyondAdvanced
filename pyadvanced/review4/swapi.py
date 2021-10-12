class Swapi:
    def __init__(self, cat, name):
        self.cat = cat
        self.name = name

    @property
    def cat(self):
        return self.__cat
    @cat.setter
    def cat(self, new_cat):
        self.__cat = new_cat
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
    def appendData(detail):
        fout = open('swapi.txt', 'at')
        print(detail, file=fout)
        fout.close()

