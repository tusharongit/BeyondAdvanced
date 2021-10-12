#
class WebPage():
    def __init__(self, title, desc):
        self.__title = title
        self.__desc = desc
    
    @property # built-in decorator
    def title(self): # get method
        return self.__title

    @title.setter # built-in decorator
    def title(self, title):
        # make sure that the title is not empty and a string
        if title != '' and type(title) == str:
            self.__title = title
        else:
            self.__title = 'NA'

    @property # built-in decorator
    def desc(self): # get method
        return self.__desc

    @desc.setter # built-in decorator
    def desc(self, desc):
        # make sure that the description is not empty and a stringg
        if desc != '' and type(desc) == str:
            self.__desc = desc
        else:
            self.__desc = 'NA'

    def showWebPageDetail(self):
        print('Title: {}; Description: {}'.format(self.__title, self.__desc))

    def logWebPageDetail(self):
        fout = open('webpages.txt', 'at')
        print('Title: {}; Description: {}'.format(self.__title, self.__desc), file=fout)
        fout.close()

if __name__ == '__main__':
    # instance of class WebPage
    w = WebPage('Home', 'Welcome to our website')
    print('Expected:\nTitle: {}; Description: {}\n'.format(w.title, w.desc))
    # w.title = '' # this uses the @property mutator
    # print('Title: {} Description: {}'.format(w.title, w.desc))
    w.showWebPageDetail()

