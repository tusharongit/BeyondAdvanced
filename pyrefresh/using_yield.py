# all generators comporehensively iterate over a collection
# (in memory of generated in demand)
# custom generators can be written using the 'yield' keyword

def genMultiples(start=1, stop=10, step=2):
    '''
    Generate increasing multiples of a range of numbers
    '''
    num = start

    while num < stop:
        yield num  # using the 'yield' keyword makes this a custom generator
        num *= step

def app():

    lx = []
    ly = []
    # x and y are instances of the custom generator
    x = genMultiples()
    y = genMultiples(3,100,4)

    for i in x:
        lx.append(i)
    print(lx)

    #print(*y)
    for i in y:
        ly.append(i)
    print(ly)


if __name__ == '__main__':
    app()
