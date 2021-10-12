import requests
import sys

# Access the endpoint API at https://jsonplaceholder.typicode.com/
# categories can be usrrs, posts, albums, photos, todos
# pass params for category and id either as sys agruments (argv) or user input
# grab the returned json, handle exceptions
# if it's a user, display latitude, longitude

def getInfo(list):
    category=list[1]
    id=list[2]
    url = 'https://jsonplaceholder.typicode.com/{}/{}'.format(category,id)
    try:
        response = requests.get(url)
        # .json as we expect a json response, alternately we can use .text or .html or .xml
        d = response.json() # d is returned as a dictionary
        if category == 'users':
            name = d['name']
            lat = d['address']['geo']['lat'] # bracket notation as d is a dictionary
            lng = d['address']['geo']['lng']
            return '{} is at lat {} long {}'.format(name, lat, lng)
        else:
            return d.text
    except Exception as err:
        return 'Something went wrong: {}'.format(err)

if __name__ == '__main__':
    # if there were no sys args, ask user for params
    if len(sys.argv) > 1: # sys.argv is a tuple of variables entered at the time of running this file from cmd
        category = sys.argv[1]
        id = sys.argv[2]
    else:
        category = input('Category:')
        id = int(float(input('Id:')))

    print(getInfo(category,id))
