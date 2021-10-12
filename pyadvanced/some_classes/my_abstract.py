# abc is the abstract base class
from abc import ABCMeta, abstractmethod, abstractproperty

# declare an abstract top class
class Shape():
    __metaclass__ = ABCMeta
    @abstractmethod
    def display(self):
        pass
    @abstractproperty
    def name(self):
        pass