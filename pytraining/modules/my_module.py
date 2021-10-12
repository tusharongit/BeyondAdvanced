# here we declare reusable functions in our module
# e.g. take a bunch of numbers and return the sum

def addStuff (*args):
    #print(args)
    total = 0
    for num in args:
        if type(num) == int or type(num) == float:
            total += num
    #print(total)
    return total


if __name__ == "__main__":
    # following code will run only if this file is being run standalone
    # e.g. for unit testing of functions in this module
    # print(addStuff (1,2,3,4,5))
    # print(addStuff(1.5,2.5,3.5,4.5,5.5))

    # nums = list(range(45,48))
    nums = []
    for i in range(45,48):
        nums.append(i)
    # print(addStuff(nums))
    print (nums)
    print("total=",addStuff(nums))

