# we can get a memory profiler to explore perf
# 1. from memory_profiler import profile
# 2. decorate funcs using @profile
# 3. invoke by execution 

from memory_profiler import profile
import collections

@profile # decorator to a function for which memory profile is needed
def someFn():
    # double-ended queue
    my_deq = collections.deque('98765432')
    print('Dequeue {}'.format(my_deq))

    # we can alter members of a deque from front or back
    my_deq.append('1')
    print('Dequeue {}'.format(my_deq))

    my_deq.appendleft('0')
    print('Dequeue {}'.format(my_deq))

    my_deq.pop()
    print('Dequeue {}'.format(my_deq))

    my_deq.popleft()
    print('Dequeue {}'.format(my_deq))

if __name__ == '__main__':
    someFn()
