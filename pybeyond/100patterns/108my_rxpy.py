# Reactive Extension for Python (RxPY) is a set of libs for composing async and event-based prog

import requests
import rx
import json
from rx import operators as op

# access the API end point https://jsonplaceholder.typicode.com/users

def filterNames(x, l):
    if x['name'].startswith(l):
        return x['name']
    else:
        return '' # no match

def main():
    # ask the user what starting letter to filter on
    letter = input ('Names starting with...')
    # fetch all users from API endpoint that start with 'letter'
    content = requests.get('https://jsonplaceholder.typicode.com/users')
    # convert from JSON to python structure
    y = json.loads(content.text) # this will return a dict
    # create an rx observable
    source = rx.from_(y)
    # use the observable
    case1 = source.pipe( # this will asynchronously wait for the data to be ready
        op.filter(lambda c:filterNames(c,letter)), # c is each member in the source
        op.map(lambda a:a['name']) # a is each member in the source
    )
    # subscribe to the observable
    case1.subscribe(
        # implement next, error and complete handlers
        on_next = lambda i: print('Received {}'.format(i)),
        on_error = lambda e: print('Error {}'.format(e)),
        on_completed = lambda: print('Complete')
    )





if __name__ == '__main__':
    main()

