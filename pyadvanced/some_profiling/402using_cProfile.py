# cProfile is a performant way to profile non-trivial code
# can be invoked by: python -m <which module> -o <output file> <module to profile>
# python -m cProfile -o profiling_out 402using_cProfile.py
# 
# This file will record
# no. of calls for each method
# total times taken by that method
# time taken per call
# cumulative time

from functools import reduce

def fib1(n):
    seq = (0,1)
    for _ in range(2, n+1):
        seq += (reduce(lambda a,b: a+b, seq[-2:]),) # lambda is a way of writing a one-time inline func
    return seq[n]

def fib2(n):
    if n <= 1:
        return n
    else:
        return fib2(n-1) + fib2(n-2) # recursively call the same func

if __name__ == '__main__':
    print(fib2(36))
    print(fib1(36))
