import sys
import requests

from swapi import Swapi
from swapi_people import SwapiPeople
from swapi_planets import SwapiPlanets
from swapi_films import SwapiFilms

def validateSwapi(cat):
    swapi_tup = ('people','planets','films','species','vehicles','starships')
    if cat in swapi_tup:
        return True
    else:
        return False

def getSwapiDetail(cat, id):
    url = 'https://swapi.dev/api/{}/{}'.format(cat,id)
    try:
        response = requests.get(url)
        d = response.json() # s is returned as a dictionary
        if cat == 'people':
            name = d['name']
            height = d['height']
            #hair = d['hair_color']
            eye = d['eye_color']
            s_people = SwapiPeople(cat,name,height,eye)
            print(s_people)
        elif cat == 'planets':
            name = d['name']
            climate = d['climate']
            terrain = d['terrain']
            pop = d['population']
            s_planets = SwapiPlanets(cat, name, climate, terrain, pop)
            print(s_planets)
        elif cat == 'films':
            name = d['title']
            dir = d['director']
            pro = d['producer']
            s_films = SwapiFilms(cat, name, dir, pro)
            print(s_films)
        else:
            return d.text
    except Exception as err:
        return 'Something went wrong: {}'.format(err)

def getUserInput():
    print('An app to ping Star Wars API and get details')
    print('for people, planets, films, species, vehicles, starships')
    s_cat = input('Category: ')
    if validateSwapi(s_cat):
        s_id = input('Id: ')
        while int(float(s_id)) > 6:
            print('Try a smaller Id!')
            s_id = input('Id: ')
        getSwapiDetail(s_cat, s_id)
    else:
        print('Not a valid swapi!')

if __name__ == '__main__':
    # if file is called from cmd line call getSwapiDetail directly, otherwise ask for user input
    if len(sys.argv) > 1:
        if validateSwapi(sys.argv[1]):
            getSwapiDetail(sys.argv[1], sys.argv[2])
        else:
            print('Not a valid swapi!')
    else:
        getUserInput()
