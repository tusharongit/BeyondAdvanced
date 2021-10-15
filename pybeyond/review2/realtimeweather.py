import threading
import weathergetter
import datetime

class CityWeather(threading.Thread):
    def __init__(self, sem, city):
        threading.Thread.__init__(self)
        self.__sem = sem
        self.city = city

    def run(self):
        wg = weathergetter.WeatherGetter(self.city)
        wg.run()

if __name__ == '__main__':
    cities = ['athlone','belfast','cork','dublin','edenderry','frankfurt','galway','houston','istanbul','jakarta','kolkata','london','mumbai','nairobi','ottawa','paris','quebec']
    sem = threading.Semaphore() # optional param - how many simultaneous semaphores are allowed

    # use the semaphore in city instances
    t1 = float(datetime.datetime.now().strftime("%S"))
    for c in cities:
        cw = CityWeather(sem,c)
        cw.start()
    t2 = float(datetime.datetime.now().strftime("%S"))
    print('Weather data retrieved in {}sec'.format(t2-t1))
    
