# input category and id, fetch data from https://jsonplaceholder.typicode.com/, write to a file
# use 'requests' lib to make 'get' call from the API
# category can only be users, posts, albums, photos
# id can only be a positive number
# use try-except for exception handling and always have a default cat and id
# 

import requests
import json

import datetime

import my_modules.util as util

def getResult(inCat, inId):
    result = requests.get('https://jsonplaceholder.typicode.com/{}/{}'.format(inCat,inId))
    return result.json()

def writeToFile(inCat, inId, result_d):
    f = 'review2file.txt'
    fout = open(f,'a')  # opens a file for overwriting and names the file access object as fout
    print (datetime.datetime.now(), file=fout)
    print('category \'{}\' . id {}'.format(inCat,inId,f), file=fout)
    print (result_d, file=fout)
    fout.close()
    print('All details for category \'{}\' and id {} have been written to file \'{}\''.format(inCat,inId,f))

if __name__ == '__main__':

    # define all categories
    allCats = ('users', 'posts', 'albums', 'photos')

    # default category is users; default id=1
    defCat = 'users'
    defId = 1

    # input category from user, 0 to exit
    inCat = input('Enter a category from {} or 0 to exit: '.format(allCats))
    if inCat == '0':
        print('Bye!')
        quit()
    else:
        inCat = util.checkCat(inCat, defCat, allCats)  # call checkCat util to verify
    
    # input id from user, 0 to exit
    inId = input('Enter an id (number) or 0 to exit: ')
    if inId == '0':
        print('Bye!')
        quit()
    else:
        inId = util.checkInt(inId)  # call checkInt util to verify

    #print('id:',inId,'\ncategory:',inCat)

    #print (result_d)
    result_d = getResult(inCat, inId)

    writeToFile(inCat, inId, result_d)

    if inCat == defCat:
        more = input('Do you want to additionally retrieve all posts for this user (y/n)')
        if more == 'y' or more == 'yes':
            writeToFile(inCat, inId)
        else:
            print('Bye!')
            quit()

    




    
    

