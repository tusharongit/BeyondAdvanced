# # using for
# weekDays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# print("Weekdays:")
# for item in weekDays:
#     print(item)

# myName = "Tushar"
# print("My name is:")
# for i in myName:
#     print(i)

# myDict = {"fname":"Tushar", "lname":"Mathur", "eircode":"N37 RD00", "phone": 3530870918477, "coord": [0.02,52.3]}
# for x in myDict:
#     print(x, ":", myDict[x])

# range
# for i in range(0,20,3): #start, stop before, step
#     print(i)

# for i in range(20,0,-3): #start, stop before, step
#     print(i)

# generator
# num_list = []
# print(num_list)
# num_list.append(1)
# num_list.append(2)
# num_list.append(3)
# num_list.append(5)
# num_list.append(8)
# num_list.append(13)
# for i in range (1,20):
#     num_list.append(i*2)
# print(num_list)

# num_list = list(range(1,20))
# print(num_list)

num_list_sq = [num**2 for num in range(0,10)]
#print("Squares:", num_list_sq)

num_list_ev = [num for num in range(0,100,2)] # [num for num in range(0,100) if num%2==0]
#print("Evens:", num_list_ev)

num_list_od = [num for num in range(1,100,2)] # [num for num in range(0,100) if num%2==1]
#print("Odds:", num_list_od)

num_list_pr = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
#print("Primes:", num_list_pr)

num = int(input("Your number (0 - 100):"))

if (num in num_list_sq):
    print(num, "is a sqaure")

if (num in num_list_ev):
    print(num, "is an even number")

if (num in num_list_od):
    print(num, "is an odd number")

if (num in num_list_pr):
    print(num, "is a prime")
