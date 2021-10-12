# __iter__ is built into python
# it lets us iterate

l = [1, 7, 11, 24]
l_iter = iter(l) # iter unpacks the list
print(l_iter)
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
# print(l_iter.__next__())

# can we directlty access __next__ on a list?
# print(l.__next__()) # fails; list has no yield

# iter has built-in reversing capabilities

r = reversed(l)
for i in r:
    print (i)

