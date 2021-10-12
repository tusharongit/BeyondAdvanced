
def my_range (first=0, last=100, step=1):
    num = first
    while num < last:
        yield num # using yield instead of return
        num += step
        step += num

if __name__ == '__main__':
    s = {num for num in range(-10,10) if num%3 == 0}
    print(s)
    # use our own geenrator
    i = my_range()
    print(i) # generator object
    for item in i:
        print (item) # calls yield for the next value in range

    t = my_range(99,1000, 5)
    # we can pick the next value whenever we want
    print(t.__next__())
    print(t.__next__())
    print(t.__next__())
    print(t.__next__())
    print(t.__next__()) # fails; nothing next to yield
    
