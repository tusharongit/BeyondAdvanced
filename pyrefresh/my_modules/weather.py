# class and methods for creating and validating weather data

class Weather:
    def __init__(self, temp, desc):
        self.temp = temp
        self.desc = desc


    @property  # property for temperature
    def temp(self):
        return self.__temp

    @temp.setter  # behaves as if email is a directly accessible/ mutable property, but internally calls the property defined above
    def temp(self, temp):
        self.__tempC = temp
        self.__tempF = (temp*9/5) + 32
        self.__tempK = temp + 273


    @property  # property for description
    def desc(self):
        return self.__desc

    @desc.setter  # behaves as if email is a directly accessible/ mutable property, but internally calls the property defined above
    def desc(self, desc):
        desc_t = ('clear', 'sunny', 'partly cloudy', 'cloudy', 'windy', 'rainy', 'snowy')
        if desc in desc_t:
            self.__desc = desc
        else:
            self.__desc = 'partly cloudy'

    
    def __str__(self):
        prn = 'Temperature is {}c and {}'.format(self.__tempC, self.__desc)
        return prn



if __name__ == '__main__':
    w1 = Weather(25, 'sunny')
    w2 = Weather(20, 'meatballs')
    print(w1, w2)