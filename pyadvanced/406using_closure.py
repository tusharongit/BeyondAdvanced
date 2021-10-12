# closure refers to the moment we actually invoke a function

def minions(say):
    def inner():
        return 'Minion says {}'.format(say)
    return inner

if __name__ == '__main__':
    r = minions('Heehee')
    s = minions('Haahaaaa')
    print(r(), s())