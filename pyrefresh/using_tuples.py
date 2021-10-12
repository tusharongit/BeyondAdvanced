# a tuple is an indexed immutable collection of any types

t = (5, True, 3.2, 'ooooh')
l = [5, True, 3.2, 'ooooh']
s = 'this is a string'

# tuple unpacking
m, n, o, p = t

# list unpacking
a, b, c, d = l

print(a,b,c,d)
print(m,n,o,p)

#strings cannot be unpacked
w, x, y, z = s
print(w, x, y, z) # fails

