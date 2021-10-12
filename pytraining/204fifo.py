# file handling

# fout is the file object
# wt = (over)write text
# at = append text
# xt = exclusive text, i.e. fail if file exists

fout = open('snip.txt', 'at')
print("This is a text snippet", file=fout, end="\n") # end is optional delimiter and defaults to \n
fout.close ()

# try:
#     fout = open('snip.txt', 'at')
#     print ("This is a text snippet!", file=fout, end="") # end is optional delimiter and defaults to \n
#     fout.close ()
# except FileExistsError: # when exception occurs, this pice of code will execute (handling exceptions)
#     print("Cannot override! File already exists. Try without xt mode.")
# except Exception as err:
#     print("Something bad happened! Check for", err)
# finally:
#     print("We're done here")

# rt = readt text
# fin = open("snip.txt", "rt")
# getiIt = fin.read()
# fin.close()
# print(getiIt)


# read and write binary files
bdata = bytes(range(0,256)) # bytes is a data type
print(len(bdata))

fout = open ("binfile", "wb") # wb = write binary
fout.write(bdata)
fout.close()