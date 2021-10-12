n = 42
f = 7.03
s = "cheese"

print("The value of n is {}, f is {} and s is {}".format(n, f, s)) # format passes postional args

print("s = {2}, n is {0} and f is {1}".format(n, f, s)) # using the postional args

# or use a dictionary
d = {"n": 21, "f": 14.06, "s":"mac"}
print("Using dict, n={0[n]}, f={0[f]} and s={0[s]}".format(d))

# cast or format
print("Casting {0:12d}, {1:0.3f}, {2:s}".format(n,f,s))
