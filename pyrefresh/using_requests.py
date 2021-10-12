# making calls to external API end-points
import requests
import json

#import my_modules.util
#import my_modules.util as u
from my_modules.util import checkInt

def main(n=1):
    result = requests.get('https://jsonplaceholder.typicode.com/photos/{}'.format(n))
    result_d = result.json()
    print('id:',n,'\ntitle: ',result_d['title'])

if __name__ == '__main__':
    # ask user for a num
    n = input('enter a num: ')

    # validate whether this is a num, by importing the checkInt utility
    # n = my_modules.util.checkInt(n)
    # n = u.checkInt(n)
    n = checkInt(n)

    # call the main function
    main(n)