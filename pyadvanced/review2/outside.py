# ask the user the city-country they want to see the weather for
# pre-populated list or ask the user to say

import requests
import json
from day2classes.weather import Weather

def getWeather(city,cntry):
    apiendpoint = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'.format(city,cntry)
    w_json = json.loads(requests.get(apiendpoint).text)
    
    w_desc = w_json['weather'][0]['description']
    w_temp = w_json['main']['temp']
    w_feel = w_json['main']['feels_like']
    w_wspd = w_json['wind']['speed']
    
    outside = Weather(w_desc, w_temp, w_feel, w_wspd)
    print('In {}, {}, {}'.format(city, cntry, outside))


def getGlobalWeather():
    fin = open('location.txt','rt')
    locations = fin.readlines()
    fin.close()
    #print(location)
     
    for loc in locations:
        city, country = loc.split(',')
        country = country.strip()
        getWeather(city,country)

def getLocalWeather():
    city = input('Enter city:')
    country = input('Enter country:')
    getWeather(city,country)

def reportWeather():
    whichWeather = 'A'
    while (whichWeather != 'G' and whichWeather != 'L'):
        whichWeather = input('Would you like to know Global (G) weather of Local (L)?')
        if whichWeather == 'G':
            getGlobalWeather()
        elif whichWeather == 'L':
            getLocalWeather()


def testThisCode():
    city = 'London'
    country = 'UK'
    apiendpoint = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'.format(city,country)
    #w = requests.get(apiendpoint)
    #print(weather.text)
    w_json = json.loads(requests.get(apiendpoint).text)

    w_desc = w_json['weather'][0]['description']
    w_temp = w_json['main']['temp']
    w_feel = w_json['main']['feels_like']
    w_wspd = w_json['wind']['speed']
    
    print('desc =',w_desc)
    print('temp =',w_temp)
    print('feel =',w_feel)
    print('wspd =',w_wspd)

    outside = Weather(w_desc, w_temp, w_feel, w_wspd)
    print('In {}, {}, {}'.format(city, country, outside))


if __name__ == '__main__':
    #pass
    #testThisCode()
    reportWeather()

