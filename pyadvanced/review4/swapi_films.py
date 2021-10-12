from swapi import Swapi

class SwapiFilms (Swapi):
    def __init__(self, cat, name, dir, pro):
        super().__init__(cat, name)
        self.dir = dir
        self.pro = pro

    @property
    def dir(self):
        return self.__dir
    @dir.setter
    def dir(self, new_dir):
        self.__dir = new_dir

    @property
    def pro(self):
        return self.__pro
    @pro.setter
    def pro(self, new_pro):
        self.__pro = new_pro

    def __str__(self):
        return '{} was directed by {} and produced by {}!\n'.format(self.name, self.dir, self.pro)
    