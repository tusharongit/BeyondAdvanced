#
class WebSite(object):
    def __init__(self, name, url, pages, users):
        self.__name = name
        self.__url = url
        self.__pages = pages
        self.__users = users
    
    @property # built-in decorator
    def name(self): # get method
        return self.__name

    @name.setter # built-in decorator
    def name(self, name):
        # make sure that the title is not empty and a string
        if name != '' and type(name) == str:
            self.__name = name
        else:
            self.__name = 'NA'

    @property # built-in decorator
    def url(self): # get method
        return self.__url

    @url.setter # built-in decorator
    def url(self, url):
        # make sure that the description is not empty and a stringg
        if url != '' and type(url) == str:
            self.__url = url
        else:
            self.__url = 'www.unknown.web'

    def showWebSiteDetail(self):
        print('Website: {}\nURL: {}'.format(self.__name, self.__url))

    def logWebSiteDetail(self):
        fout = open('website.txt', 'wt')
        print('Title: {}; Description: {}'.format(self.__name, self.__url), file=fout)
        fout.close()

if __name__ == '__main__':
    # instance of class WebPage
    w = WebPage('Home', 'Welcome to our website')
    print('Expected:\nTitle: {}; Description: {}\n'.format(w.title, w.desc))
    # w.title = '' # this uses the @property mutator
    # print('Title: {} Description: {}'.format(w.title, w.desc))
    w.showWebPageDetail()

