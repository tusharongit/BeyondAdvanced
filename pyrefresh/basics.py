# here is a Python comment
a = 2 # an integer
b = 5

c = a/b # returns floating point value in py 3; in py 2 this would return an integer ie. respects data types
#print(c) 

c = b//a # returns the integer part of division
#print(c) 

c = b%a # returns the remainder part of division
#print(c) 

c = b**a # returns the power of
#print(c) 

c = 'hello' # a string
#print (c)

# collections
s = 'this is a string of characters' # a string
#print (s[13]) # [index]
#print (s[13:20]) # [start from : stop before]
#print (s[13:20:2]) # [start from : stop before : step]
# reverse
#print (s[::-1])

# lists and tuples
l = [1, False, a] # list, mutable
t = (1, False, a) # tuple, immutable
#print ('list',l)
#print ('tuple',t)

l[2] = b
#print ('changed list',l)

#t[2] = b = fails, can't mutate
#print (t)

l = [1, False, a, (200,300,400), 'new', 4.5, True, [55,66,77,88]] # list, mutable
#print ('new list',l)
l[7][1] = 11
#print ('changed new list',l)

#print (type(a), type(b), type(c), type(s), type(l), type(t))

# user input
u = input('what is your fav num? ')
print ('You meant ',u) # input is always a string

#type casting
uint = int(u)
ufloat = float(u)

print (type(u), u, type(uint), uint, type(ufloat), ufloat)

tup_one = (2,) # single member-tuple, not (2)


