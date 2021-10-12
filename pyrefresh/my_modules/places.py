# class and methods for creating and validating cities and countries

class Place:
    def __init__(self, country, city):
        self.country = country
        self.city = city


    @property  # property for country
    def country(self):
        return self.__country

    @country.setter  # check if country is in this list, default to IE
    def country(self, country):
        country_t = ('ie', 'gb', 'fr', 'de', 'aus', 'usa')
        if country in country_t:
            self.__country = country.upper()
        else:
            self.__country = 'IE'


    @property  # property for city
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city.title()

    def __str__(self):
        plc = '{}-{}'.format(self.__city, self.__country)
        return plc

if __name__ == '__main__':
    p1 = Place('usa', 'athlone')
    p2 = Place(20, 'galway')
    print(p1, p2)