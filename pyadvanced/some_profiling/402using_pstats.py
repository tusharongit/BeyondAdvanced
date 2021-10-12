# use pstats to open and read the output of a cProfile session

import pstats

def main():
    p = pstats.Stats('some_profiling\profiling_out')
    p.print_stats()

if __name__ == '__main__':
    main()