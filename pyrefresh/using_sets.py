# a set is like a dictionary but with no keys, just UNIQUE values

s = {0, False, 8.8, 3, 2, 4, True, 3.2, 1}
s.add(1.55)
#print(s)

num = {0,1,2,3,4,5,6,7,8,9,10}
fib = {0,1,2,3,5,8,13}

for i in num:
    if i in fib:
        print(i, 'isa fib')
    else:
        print(i, 'not fib')

q = input('check a value for fibonacci number less than 21: ')
if q.isnumeric() and int(q) in fib:
    print('yes, {} isa fib'.format(q))
else:
    print('no, {} not fib'.format(q))