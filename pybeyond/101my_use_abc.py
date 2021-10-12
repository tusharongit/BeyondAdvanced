# exploring Abstract Base Class collection
# particularly the Container class

from collections.abc import Container

# class to check if a member is an odd (or not) number
class OddContainer(Container): # explicitly extends the Container class
    def __contains__(self, __x): # override the 'in' operator; returns boolean
        if not isinstance(__x, int) or not __x%2: # not x%2 is same as x%2 != 0
            return False
        return True # if not divisible by 2 it is an odd number

# class to check if a member is an even (or not) number
class EvenContainer: # implicitly extends the Container class
    def __contains__(self, __x): # override the 'in' operator; returns boolean
        if not isinstance(__x, int) or __x%2: # x%2 is same as x%2 == 0
            return False
        return True # if divisible by 2 it is an even number


if __name__ == '__main__':
    oc1 = OddContainer()
    ec1 = EvenContainer()
    print('110:',110 in oc1) # assert True; calls the __contains__ internally
    print('110:',110 in ec1) # assert True; calls the __contains__ internally
    print(Container.__abstractmethods__)
    print(issubclass(OddContainer, Container)) # is OddContainer a sub-class of Container? True, explicitly extends
    print(issubclass(EvenContainer, Container)) # is EvenContainer a sub-class of Container? True, implicit