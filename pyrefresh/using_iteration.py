# iterators

l = [5, 4, 3, True, (1,), 'hi']

i=0
#print('i is', i)

# for iteration
for item in l:  # colon indicates starts of a code block
    #print(item) #each line of the code block is indented
    #print(type(item))
    i = i+1

#print('i is', i)
# code block ends when indentation ends

# range object can also be used for iteration
r = range (99)
#print(r, type(r))

#for i in range(-9,10,3): # start, stop before, step
    #print(i)


# iterating over collections
s = 'not long  until lunch time'
d = {'name':'Ada', 'age':35, 'vaxed':True}

#for c in s:
    #print(c)

#for item in d:
    #print(item)
    #print(item, d[item])

#for key, value in d.items():
    #print(key, value)

# we can generate members as we need them
#my_gen = ( num**0.5 for num in range(-10*10, 10*10) ) # a tuple generator for sq root of all nums -110 to 110
#print(type(my_gen))

#for r in my_gen:
    #print(r) # generates the numbers as needed, then discarded, not stored

# mini-challenge - generate all even nums 0-100 without using step
evens = ( num*2 for num in range (0,51))
for r in evens:
    print(r)

# we can combine 'if' logic in custom generators
odds = ( num for num in range (0,100) if num%2 != 0)
for r in odds:
    print(r)
    