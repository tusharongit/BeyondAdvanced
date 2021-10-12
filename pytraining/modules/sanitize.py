# to ensure every data member is a capitalized string

def makeCaps (var):
     return var.title()

def cleanup (data):
    if type(data) != str:
        data = str(data)
    return makeCaps(data)

if __name__ == "__main__":
    # print(makeCaps("a"))
    # print(makeCaps("abcd"))
    # x = "a"
    # x = "abcd efgh"
    x = 23
    # x = False
    print(x,type(x))
    x = cleanup(x)
    print(x,type(x))
