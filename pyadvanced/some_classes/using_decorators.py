# creating your own custom decorators
# popular built-in decorators are
# @property (for getter)
# @setter
# @abstractmethod
# @abstractproperty

def show_args(func): # passing a function as a parameter
    def new_func(*args, **kwargs):
        print('Running function {}'.format(func.__name__))
        print('Positional *args: {}'.format(args)) # tuple
        print('Keyword **kwargs: {}'.format(kwargs)) # dict
        return func(*args, **kwargs)
    return new_func

# simple metod to add two ints
@show_args # automatically runs the fuction, passing in the decorated method
def add_ints(a, b):
    if isinstance(a, int) and type(b) == int:
        return a+b
    else:
        return 'fail'

if __name__ == '__main__':
    
    print(add_ints(3,4)) # positional args
    print(add_ints(b=3,a=4)) # keyword args