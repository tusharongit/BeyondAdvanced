# deque is a double-ended queue
# we can access both ends to append or remove members
from collections import deque

def palindrome(word): # madamimadam, racecar
    dq = deque(word)
    palin = 0
    while len(dq) > 1:
        if dq.popleft() == dq.pop(): # pop and popleft mutate dq
            palin += 0
        else:
            palin += 1
    return bool(palin)

if __name__ == '__main__':
    print(palindrome('madamimadam'))
    print(palindrome('racecar'))
    print(palindrome('palindrome'))