# ask the user the city-country they want to see the weather for
# pre-populated list or ask the user to say

import requests
import json
import sys
from weather import Weather

def getWeather(city,cntry):
    apiendpoint = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'.format(city,cntry)
    w_json = json.loads(requests.get(apiendpoint).text)
    
    w_desc = w_json['weather'][0]['description']
    w_temp = w_json['main']['temp']
    w_feel = w_json['main']['feels_like']
    w_wspd = w_json['wind']['speed']
    
    outside = Weather(w_desc, w_temp, w_feel, w_wspd)
    return 'In {}, {}, {}'.format(city, cntry, outside)

# get weather for all cities in locations.txt
def getGlobalWeather():
    fin = open('location.txt','rt')
    locations = fin.readlines()
    fin.close()
    w_str = ''
    #print(location)
     
    for loc in locations:
        city, country = loc.split(',')
        country = country.strip()
        w_str = w_str + getWeather(city,country) + '\n'
    
    return w_str

# get weather for input city and country
def getLocalWeather(city, country):
    #city = input('Enter city:')
    #country = input('Enter country:')
    return getWeather(city,country)

# main method to call
def reportWeather(list):
    if len(list) > 2:
        # 3 args weather, local, city and country
        return getLocalWeather(list[2],list[3])
    elif len(list) > 1:
        # 2 args weather, global
        return getGlobalWeather()
    else:
        return getGlobalWeather()


def testThisCode(city,country):
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
    if len(sys.argv) > 3:
        # 3 args after filename are weather, city and country
        print(getLocalWeather(sys.argv[2],sys.argv[3]))
    elif len(sys.argv) > 2:
        # 2 args after filename are weather, global
        print(getGlobalWeather())
    else:
        print(getGlobalWeather())
        #testThisCode('London', 'UK')
    

