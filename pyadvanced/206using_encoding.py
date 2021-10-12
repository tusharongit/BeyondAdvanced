# a set of classes to encode our data structures
import json

class Item:
    def __init__(self, name, cost):
        self.name = name # calls the setter method below
        self.cost = cost # calls the setter method below

    def __str__(self):
        return 'This instance of Item object has name {} and cost {}'.format(self.name, self.cost) # calls the getter methods

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self,new_cost):
        self.__cost = new_cost

class ItemEncoder(json.JSONEncoder): # this class enherits from json.JSONEncoder
    def default(self, obj_to_encode): # override the default encoding method of JSONEncoder
        if isinstance(obj_to_encode, Item): # check it is for class Item
            return obj_to_encode.__dict__ # return a dictionary of the object
        else:
            # if type is not of type Item then use default of base class to handle an exception
            return json.JSONEncoder.default(self, obj_to_encode)


if __name__ == '__main__':
    laptop = Item('laptop', 899)
    #itemJSON = json.dumps(laptop) # uses default JSON encoding; fails, not serializable
    #print (type(itemJSON), itemJSON)
    itemJSON_i = json.dumps(laptop, cls=ItemEncoder) # uses our Item Encoder
    print (type(itemJSON_i), itemJSON_i)
