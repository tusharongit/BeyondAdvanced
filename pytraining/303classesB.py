# another way to write classes, accessor and mutator methods
class WebPage(): # implicitly inherit from object
    def __init__(self, title, desc):
        self.__title = title
        self.__desc = desc
    @property # this is a built-in decorator
    def title(self): # this is the getter method
        return self.__title
    @title.setter # another built-in decorator - required if we want a genuine mutator method
    def title(self, title):
        # we will make sure that the title is a non-empty string
        if title != '' and type(title) == str:
            self.__title = title
        else:
            self.__title = 'NA'
    @property # this is a built-in decorator
    def desc(self): # this is the getter method
        return self.__desc
    @desc.setter # another built-in decorator
    def desc(self, desc):
        # we will make sure that the description is a non-empty string
        if desc != '' and type(desc) == str:
            self.__desc = desc
        else:
            self.__desc = 'NA'

if __name__ == '__main__':
    # create instances
    w = WebPage('Home', 'Welcome to our website')
    print('Title: {} Description: {}'.format(w.title, w.desc))
    w.title = '' # this uses the @property mutator
    print('Title: {} Description: {}'.format(w.title, w.desc))

