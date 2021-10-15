# more accurate time capabilities are avl using timeit
# timeit ignores non-python time delays, ie only counts time taken by python to execute code

import random
import time
import timeit

# a function to decorate a function we need to accurately time
def timethis(func):
    def func_timer(*args, **kwargs):
        start_time = timeit.default_timer()
        value = func(*args, **kwargs)
        run_time = timeit.default_timer() - start_time
        print('Function {} took {}sec'.format(func.__name__, run_time))
        return value
    return func_timer

@timethis
def long_runner():
    for x in range(9):
        sleep_time = random.choice(range(1,3))
        time.sleep(sleep_time)

@timethis
def count_up():
    for i in range(1, 100):
        x = i

@timethis
def count_down():
    for j in range(100, 1, -1):
        y = j



if __name__ == '__main__':
    long_runner()
    count_down()
    count_up()
