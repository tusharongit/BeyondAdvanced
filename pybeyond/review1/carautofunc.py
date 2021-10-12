import autowiper
import autolights

class AutoFunc: # this is our observable (subject)
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, new_sub): # join a new subscriber
        self.__subscribers.append(new_sub)

    def detach(self):  # remove the most recent subscriber
        self.__subscribers.pop()

    def subscribers(self): # iterate over all subscribers
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return ('News: {}'.format(self.__latestNews))

# some subscribers (these are our observers)
class autoLights:
    def __init__(self, pub):
        self.publisher = pub
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class autoWipers:
    def __init__(self, pub):
        self.publisher = pub
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    carAF = AutoFunc()
    # iterate over a collection of subscribers and notify each
    outside = {}
    outside[0] = {'dark':True, 'rain':'none', 'text':'It has become dark as rain clouds are approaching'}
    outside[1] = {'dark':True, 'rain':'light', 'text':'It has started to rain now'}
    outside[2] = {'dark':True, 'rain':'heavy', 'text':'It is very dark now with heavy rain'}
    outside[3] = {'dark':False, 'rain':'light', 'text':'It is sunny now with light rain'}
    outside[4] = {'dark':False, 'rain':'none', 'text':'It is sunny and rain has stopped'}
    for item in outside:
        #
        '''
        gdfg
        '''
        carAF.notifySubscribers()
        