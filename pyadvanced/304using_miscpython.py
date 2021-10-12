# named tuple, zip, deque, etc.

from collections import namedtuple

#a normal tuple
tup_normal = (True,)

#a named tuple
Duck = namedtuple('Duck','bill tail')

d1 = Duck ('long', 'short')
d2 = Duck ('wide', 'short')
d3 = Duck ('short', 'long')
print (d1.bill)

d5 = d1._replace(tail='medium', bill='orange')
print (d5.bill)

build = {'bill':'orange', 'tail':'wiggly'} # dictionary
d4 = Duck(**build)
print(d4)

# zip - not related to compression
days = ('Mon','Tue','Wed','Thu','Fri')
fruits = ['banana','orange','kiwi','grape']
drinks = ('coffee','tea','juice','water')
after = ['tiramisu','ice-cream','pie']

j = zip(days,fruits,drinks,after) # new collection

#iterate over the new collection j
for d, f, dr, a in j:
    print('On {} I ate {} with {} and finally {}'.format(d,f,dr,a))
