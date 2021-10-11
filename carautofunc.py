class AutoPublisher: # this is our observable (subject)
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
class EmailSubscriber:
    def __init__(self, pub):
        self.publisher = pub
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class PrintSubsciber:
    def __init__(self, pub):
        self.publisher = pub
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class MediaSubscriber:
    def __init__(self, pub):
        self.publisher = pub
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

if __name__ == '__main__':
    news_publisher = NewsPublisher()
    i = 0
    # iterate over a collection of subscribers and notify each
    for Subscriber in [MediaSubscriber, PrintSubsciber, EmailSubscriber]:
        i += 1
        Subscriber(news_publisher)
        news_publisher.addNews('{}: Something newsworthy just happened!'.format(i))
        news_publisher.notifySubscribers()
        