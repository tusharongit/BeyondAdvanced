# using the Factory design patterns
# The Simple Factory Pattern:
#  creates objects of diff types rather than direct obj instatntiation
# The Factory Method Pattern:
#  responsibility for obj creation is deferred to subclasses

from abc import ABCMeta, abstractmethod

class Animal(): # factory
    @abstractmethod
    def do_say(self):
        pass

class Bat(Animal):
    def do_say(self):
        print('____')

class Cat(Animal):
    def do_say(self):
        print('meow')

class Dog(Animal):
    def do_say(self):
        print('woof')

# factory to create animals
class CreatureFactory():
    def make_sound(self, object_type):
        return eval(object_type)().do_say() # eval(object_type) will come with Bat/ Cat/ Dog

if __name__ == '__main__':
    cf = CreatureFactory()
    animal = input('Which creature?')
    cf.make_sound(animal)

