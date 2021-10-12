# placeholder code
def wip_func():
    pass


# use continue and quit
var_cont = 0
var_quit = 0

def doStuff_cont():
    for i in range(10, 16):
        if (i == 13):
            print('unlucky, continue...')
            continue
        var_cont = i
        print('continue: ', var_cont)
        

def doStuff_quit():
    for i in range(10, 16):
        if (i == 13):
            print('unlucky, quitting...')
            quit()
        var_quit = i
        print('quit(): ', var_quit)

print('start in the main')
doStuff_cont()
#doStuff_quit() # if we call doStuff_quit method it stops the program when in encounters quit(), so 'back in the main' wont print
print('back in the main')

#s = '    a string    '
#print(s)
#print(s.upper())
#print(s)
#print(s.strip())
#print(s)