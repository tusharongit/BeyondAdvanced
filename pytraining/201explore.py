# import sys

# print(sys.maxsize)
# print(sys.float_info)

# import pandas as pd

# print(sys)

var = "This is a GLOBAL variable"

def method():
    global var
    print ("2", var)
    var = "This is a LOCAL variable"
    print ("3", var)

print("1", var)

method()

print("4", var)


