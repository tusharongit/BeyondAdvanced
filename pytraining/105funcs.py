# functions

# # given x and y, return r (hypotenuse) for a right-angled traingle

# def find_hypot(b=3, h=4):
#     r = (b*b + h*h)**0.5  # pythagoras theorum: hypot = sq root of (base sq + height sq)
#     print("For a right-angled triange, with base", b, "and height", h, "the hypotenuse is ...")
#     return r # if we don't return anything, it defaults to None

# base = 3
# height = 4
# hypot = find_hypot(base,height)
# print(hypot)

# base = int(input("Enter base:"))
# height = int(input("Enter height:"))

# hypot = find_hypot(base,height)
# print(hypot)

# hypot = find_hypot(h=base,b=height)
# print(hypot)

# #positional arguments

# def demo1(args):
#     print(args)

# def demo2(*args):
#     print(args)

# demo1([base, height, hypot])
# demo2(base, height, hypot)

# # keyword arguments
# # we can also gather together any keuword args
# # the double asterisk **kwargs gathers together every keyword argumanr into a dictionary

# def useKW(**kwargs):
#     print(kwargs)

# useKW(name="Enid", age=42, geo=[-0.3, 53.0])

# usings args and kwargs togeher

def useful(*args, **kwargs):
    # declare the types of each argument
    # if len(args) > 0:
    #     for item in args:
    #         print(item,type(item))
    # print the types of each keywork argument
    if len(kwargs) > 0:
        for item in kwargs:
            print(item,type(item))
        for key in kwargs:
            print(key,type(kwargs[key]))


# useful(6,7,8)
# useful(6,7,8,value=9.0)
useful(6,7,8,value=9.0, geo=(-0.2, 51))

# triple quotes or doc string

sentense1="""
triple quotes allow us to
write a long text or paragraph
using "quotes" and preserving
new line chars

even

over

multiple


line
s
s
s
s
which is commeon for\ndocumentation purposes
"""
print(sentense1)

sentense2='''
triple single quotes
are the same as\ntriple double quotes
'''
print(sentense2)