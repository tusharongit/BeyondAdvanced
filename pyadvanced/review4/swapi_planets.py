from swapi import Swapi

class SwapiPlanets (Swapi):
    def __init__(self, cat, name, climate, terrain, pop):
        super().__init__(cat, name)
        self.climate = climate
        self.terrain = terrain
        self.pop = pop
    
    @property
    def climate(self):
        return self.__climate
    @climate.setter
    def climate(self, new_climate):
        self.__climate = new_climate

    @property
    def terrain(self):
        return self.__terrain
    @terrain.setter
    def terrain(self, new_terrain):
        self.__terrain = new_terrain

    @property
    def pop(self):
        return self.__pop
    @pop.setter
    def pop(self, new_pop):
        self.__pop = new_pop

    def __str__(self):
        self.appendData('{} has {} climate with {} terrain and a population of {}!\n'.format(self.name, self.climate, self.terrain, self.pop))
    
if __name__ == '__main__':
    s_planets = SwapiPlanets('cat', 'name', 'climate', 'terrain', 'pop')
    print(s_planets)
