# file input file output

def main():
    # create a file access object
    fout = open('out.txt', 'at') # append text; wt = write text; xt = exclusive, fails if file exists
    # print to file instead of printing on screen
    print('here is some text', file=fout)
    fout.close()

def my_read():
    # create a file access object
    fin = open('out.txt', 'rt') # read text
    received = fin.read()
    fin.close()
    print(received)


if __name__ == '__main__':
    main() # write some text
    my_read() # read it back

