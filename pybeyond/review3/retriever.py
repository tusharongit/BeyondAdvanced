from threading import Thread
import json
import requests
import datetime
from memory_profiler import profile

class WeatherGetter (Thread):
    def __init__(self, city):
        self.city = city
    
    def formatLoc(self):
        text = '\n{}: {}\n'.format(self.city.title(),self.loc)
        return text

    def formatWeather(self):
        text = 'Weather is {}. Temperature is {}C feels like {}C with a windspeed of {}mph'.format(self.cond, self.temp, self.feel, self.wspd)
        return text

    def formatData(self):
        daymon = datetime.datetime.now().strftime("%d %b ")
        timenow = datetime.datetime.now().strftime("%H:%M")
        stamp = daymon + timenow
        text = self.formatLoc() + '[{}]'.format(stamp)
        text += self.formatWeather()
        return text

    def writeToFile(self):
        fout = open('weather.txt','a')
        print(self.formatData(), file=fout)
        fout.close()

    def getData(self):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.city + '&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'
        res = requests.get(url)
        #print (res.text)
        data = json.loads(res.text)

        self.lon = data['coord']['lon']
        self.lat = data['coord']['lat']
        self.loc = 'https://www.google.co.uk/maps/place/' + str(self.lon) + ',' + str(self.lat)

        self.temp = data['main']['temp']
        self.feel = data['main']['feels_like']
        self.main = data['weather'][0]['main']
        self.cond = data['weather'][0]['description']
        self.wspd = data['wind']['speed']

        print(self.formatData())
        

if __name__ == '__main__':
    cities = ['athlone','belfast','cork','dublin','edenderry','frankfurt','galway','houston','istanbul','jakarta','kolkata','london','mumbai','nairobi','ottawa','paris','quebec']
    t1 = float(datetime.datetime.now().strftime("%S"))
    for c in cities:
        wg = WeatherGetter(c)
        wg.getData()
    t2 = float(datetime.datetime.now().strftime("%S"))
    print('Weather data retrieved in {}sec'.format(t2-t1))