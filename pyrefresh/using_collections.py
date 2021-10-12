# lists
l = list() # empty list initialized
#print('empty list' , l, type(l))

l = [7,6,5,4,3]
#print('list' , l)

l.append(99)
#print('list' , l)

l.insert(1, 'new')
#print('list' , l)

w = l.pop()
#print('popped', w)
#print('list' , l)

r = l.remove('new')
#print('list' , l)

t = tuple(l)
#print('tuple' , t, type(t))


# Dictionary - a non-indexed non-ordered collection of values
d = {'first':'Tushar', 'last':'Mathur', 'age':39, 'member':True, 'score':[88,95,92,82,99]}
print(type(d), d)
d['status'] = t
print(d.keys(), d.values(), type(d))
#print(d[2]) # error as dictionary is not indexed


