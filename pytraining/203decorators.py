# imports go at the top

# define functions here

def document_it(func):
    def new_func(*args, **kwargs):
        # here is the code to document any function we might want to know about
        print("The running function is called", func.__name__)
        print("The docstring is", func.__doc__)
        if len(args)> 0:
            print("The positional arguments are", args)
        else:
            print("No positional arguments")
        if len(kwargs)> 0:
            print("The keyword arguments are", kwargs)
        else:
            print("No keyword arguments")
        result = func(*args, **kwargs)
        print("Result of the function is", result)
        return result
    return new_func # since we're returning the function, not calling the function

def square_it(func):
    def new_function(*args, **kwargs):
        
        """
        This is the doc string for new_function
        """
        
        result = func(*args, **kwargs)
        return result * result
    return new_function

@document_it # decorator
@square_it
def add_ints(a, b, x=0):
    return a+b


# immediate code
if __name__ == "__main__":
    # eg = document_it(add_ints) # pass the target function as param
    # # eg (5, 6)
    # eg (5, 6, x=True)
    
    newVar=add_ints(2,3,x=False)
    # print (newVar)

