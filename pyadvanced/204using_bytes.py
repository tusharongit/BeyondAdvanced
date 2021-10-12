# handling byte files
b = bytes(range(0,256)) # 0-255

print (b)

# write this to a file
fout = open('bfile.txt', 'wb') # write bytes
fout.write(b)
fout.close()

# read it back
fin = open('bfile.txt', 'rb')
get_b = fin.read()
fin.close
print(get_b)
