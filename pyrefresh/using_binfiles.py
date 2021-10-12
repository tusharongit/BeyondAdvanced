# binary files are used to efficiently store large data as binary uses less space

def main():
    # binary data
    b = bytes(range(0,256)) # all binary values 0 to 255
    #print(b)

    # file access object
    fout = open('binfile', 'wb')  # 'b' for binary file; defau;lt is 't' for text

    # write the binary to the file
    fout.write(b)
    fout.close()

    # read the data back
    fin = open('binfile','rb')  # read binary
    getBin = fin.read()
    print (getBin)
    fin.close()

if __name__ == '__main__':
    main()
