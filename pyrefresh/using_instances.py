# we can always check the data type

s = 'almost done'
print(type(s))

num = 3.2
print(type(num))

if isinstance(s, str):
    print(s, ' is a string')

if isinstance(num, (int, float)): # check data type against a tuple of possibilities
    print(num, ' is a number')