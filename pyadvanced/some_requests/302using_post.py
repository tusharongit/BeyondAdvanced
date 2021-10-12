# get and post requests

import requests

# for POST requests, we pass a data payload
def makePost():
    url = 'https://httpbin.org/post' # an echo API endpoint service
    payload = {'data':'something random','key1':'val1', 'key2':'val2'} # dict
    try:
        r = requests.post(url,payload)
        print(r.text)
    except Exception as err:
        print(err)


if __name__ == '__main__':
    makePost()