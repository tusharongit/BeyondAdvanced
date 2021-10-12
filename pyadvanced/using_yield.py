# we will access an API endpoint to grab a load of json data
# we will then expose this data via a custom generator

import requests # this gives access to HTTP API endpoints

def user_range(first=1, last=10):
    num = first
    while num <= last:
        res = requests.get('http://jsonplaceholder.typicode.com/users/{}'.format(num))
        yield res.text
        num += 1

if __name__ == '__main__':
    #users = user_range (2,5)
    #for u in users:
    #    print(u)

    # grab individuals on demand
    others = user_range(1,3)
    print(others.__next__())
    print(others.__next__())
    print(others.__next__())
    # others.__next__()

