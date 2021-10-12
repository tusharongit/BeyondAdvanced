# reading from (file in) and writing to (file out) external files

def writeToFile():
    # w = over(w)rite
    # a = (a)ppend
    fout = open('myfile.txt','w')  # opens a file for overwriting and names the file access object as fout
    print('this will print to a file', file=fout)
    fout.close()

def efficientWrite(data):
    try:
        fout = open('myfile2.txt', 'x')  # x = e(x)clusive access
        size = len(data)
        offset = 0
        chunk = 24
        while True:
            if offset > size:
                break
            else:
                fout.write(data[offset:offset+chunk])
                offset+=chunk
    except Exception as e:
        print(e)
    finally:
        print('done')

def readFromFile():
    fin = open('myfile2.txt','r')
    #readText = fin.read() # read the whole file
    readText = fin.readline()  # read one line
    print(readText)


if __name__ == '__main__':
    #writeToFile()
    s=''' Let's try this file read/write thing
    Just writing some random long text which can be written to a file.
    We will see how the file has spaces and new line conserved.
    This text should show across 3 lines.
    '''
    efficientWrite(s)
    readFromFile()
