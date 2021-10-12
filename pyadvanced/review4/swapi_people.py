from swapi import Swapi

class SwapiPeople (Swapi):
    def __init__(self, cat, name, height, eye_color):
        super().__init__(cat, name)
        self.height = height
        #self.hair_color = hair_color
        self.eye_color = eye_color
    
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, new_height):
        self.__height = new_height

#    @property
#    def hair_color(self):
#        return self.__hair_color
#    @hair_color.setter
#    def hair_color(self, new_hair_color):
#        self.__hair_color = new_hair_color

    @property
    def eye_color(self):
        return self.__eye_color
    @eye_color.setter
    def eye_color(self, new_eye_color):
        self.__eye_color = new_eye_color

    def __str__(self):
        return '{} is {}cm tall and has {} eyes!\n'.format(self.name, self.height, self.eye_color)
