# we use range, generator and comprehension to efficiently work with large collections

# comprehensions iterate thru a generator

num_l = [num for num in range(0,100,5)] # list - comrehensively iterates over the values and stores them in a list
print(num_l) # returns the list

num_g = (num for num in range(0,100,5)) # generator - comrehensively iterates over the values without persisting in memory
print(num_g) # returns a memory loc of the generator object

# we can use a generator to generate the values we need without persisting them in memory
for i in num_g:
    #print(i)
    print(i, end=',') # uses , imnstead of new line which is the default end of a print statement

# we can comprehensively iterate over every member of the dictionary
phrase = 'are we there yet'
# we can use a dictionary comprehension
counts = {letter:phrase.count(letter) for letter in phrase} # this is now a dictionary of instances of each letter in the sentense
print(counts, type(counts))

# comprehensions always have this form (if is optional):
# (expression or item in iterable if condition) # generator comprehension
# [expression or item in iterable if condition] # list comprehension
# {expression or item in iterable if condition} # dict comprehension

# set comprehension
my_set = {num for num in range (1,20) if num %3 == 1}
print(my_set, type(my_set))

