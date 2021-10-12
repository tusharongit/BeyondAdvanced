# json is Java Script Object Notation - it is Text, not JavaScript
import json
import datetime
import pickle

# here is a rather complex data structure
# a list of dictionaries
# each dictionary contains str, int, dict of bool, str, lists, etc.
a = [{'name':'PC', 'cost':500, 'detail':{'a':True, 'b':[1,2,3,4]}},{'name':'Screen','cost':250, 'detail':{'a':False, 'b':[9,8,7,6]}}]
#print(type(a))
#print (a)

# we can convert this to json
a_j = json.dumps(a) # takes the data structure and renders it as str
#print(type(a_j))
#print(a_j)

b = json.loads(a_j) # takes the str json and renders it as a list data structure
#print(type(b))
#print (b)

# json cannot handle datetime objs?
now = datetime.datetime.utcnow()
print (type(now),now)
now_str = str(now)
print(type(now_str), now_str)
#now_j = json.dumps(now) # fails, not serializable
now_j = json.dumps(now_str) # okay now
print (now_j)

# when json fails, use pickle
p = pickle.dumps(now) # pickle dumps coverts a datetime into bytes
print(type(p))
print(p)

n = pickle.loads(p) # pickle loads coverts it back into datetime
print(type(n))
print(n)
