# data can be passed by reference or by value

# simple data types always pass by value

a = 1
b = a  # b is equal to the value of a
print(a, b)

a+=2  # as vaue of a is changed, b is unchanged
print(a, b)

# complex structures pass by ref
m = [8, 7, 6]
p = m  # p refers to the same object as referred by m

print(m, p)

m[1] = 77  # as vaue of a member of m is changed, p also changes
print(m, p)
