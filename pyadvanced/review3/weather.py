class Weather:
    def __init__(self, desc, temp, feel, wspd):
        self.desc = desc # calls the setter method below
        self.temp = temp # calls the setter method below
        self.feel = feel # calls the setter method below
        self.wspd = wspd # calls the setter method below

    def __str__(self):
        return 'it is {} with temp {}c which feels like {}c from wind speed {}mph'.format(self.desc, self.temp, self.feel, self.wspd) # calls the getter methods

    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self,new_desc):
        self.__desc = new_desc

    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self,new_temp):
        self.__temp = new_temp

    @property
    def feel(self):
        return self.__feel
    @feel.setter
    def feel(self,new_feel):
        self.__feel = new_feel

    @property
    def wspd(self):
        return self.__wspd
    @wspd.setter
    def wspd(self,new_wspd):
        self.__wspd = new_wspd
