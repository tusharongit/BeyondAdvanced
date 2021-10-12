# determine if a number is larger or small than another number

a = input('a = ')
#a = int(float(input('a = ')))
b = input('b = ')
#b = int(float(input('b = ')))

if a<b: # <=, >=, ==, !=
    print('a is smaller')
elif b<a:
    print('b is smaller')
else:
    print('they\'re equal')

print(a, repr(a))
print(b, repr(b))
