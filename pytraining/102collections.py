# collection types > list, tuple, dictionary

# list[] > a mutable collection of any type/s
myList = [28, "Mon", 29, "Tue", 30, "Wed", "Python Programming", 28.09, False, [1,2,3,4]]
# print(myList)
# print(myList[6:8])
# print(myList[::-1])
# print(type(myList))
# print(type(myList[0]))
# myList[7]=29.09
# print(myList[6:8])
# print(myList[9][3]) # list of lists

# myList = [10,1000,3]
# print(myList[0]**myList[2]*myList[1])
# print(myList[0]*myList[2]**myList[1])
# var = "Variable"
# myList = list(var)
# print(myList)

myDate = "12/08/17"
myList = myDate.split("/")
print(myList)
myList.sort()
print(myList)
x, y, z = myList
print (x, y, z)

# tuple() > an immutable collection
myTuple = (28, "Mon", 29, "Tue", 30, "Wed", "Python Programming", 28, False, [1,2,3,4])
print(myTuple, type(myTuple))
# print(myTuple[6:8])
# print(myTuple[::-1])
# myTuple[7]=29.09 # cannot change
# print(myTuple[6:8])
# print(myTuple.index("Wed"))
# print(28 in myTuple)
# print(myTuple.count(28))
# print("-".join(myTuple[5:7]))

# dictionary{} > mutable collection not indexed by number, ie not ordinal
myDict = {"fname":"Tushar", "lname":"Mathur", "eircode":"N37 RD00", "phone": 3530870918477, "coord": [0.02,52.3]}
print(type(myDict), myDict)
print(myDict["eircode"])
print(myDict["coord"])
myDict["eircode"] = "N37 W560"
print(myDict["eircode"])
print(type(myDict), myDict)
print(myDict.keys())
print(myDict.values())

# keys = myDict.keys()
# print(keys[2])