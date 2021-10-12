# context manager exists in python 3
from contextlib import contextmanager
import sys

# functional programming to redirect stdout
@contextmanager # decorate the function with context manager
def stdout_redirect(new_stdout):
    orig_stdout = sys.stdout
    sys.stdout = new_stdout
    yield # yield the next available object to be written
    sys.stdout = orig_stdout

if __name__ == '__main__':
    print('print to console')
    with open('mylog.txt','a') as fobj:
        with stdout_redirect(fobj):
            print('print to file now') # context manager allows the redirection to happen
    print('back to console')