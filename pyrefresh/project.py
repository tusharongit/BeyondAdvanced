# top-level of a python project

# import the whole module
import random
# pr just the bits we need
from random import randint

#import my_modules.using_functions
from my_modules.using_functions import pythag

result=pythag()
print(result)