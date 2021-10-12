# check a named tuple is being used as intended
from collections import namedtuple

# define a named tuple
task = namedtuple('Task',['Summary','Owner','Done','Id'])

# set defaults
task.__new__.__defaults__ = (None, None, False, None)

# write tests to check intended use
def test_default():
    '''Using no params should invoke defaults'''
    t1 = task()
    t2 = task(None, None, False, None)
    assert t1 == t2

def test_mem_access():
    '''Check we can access members of task using . notation'''
    t3 = task('Learn Python', 'Agnes')
    assert t3.Summary == 'Learn Python'
    assert t3.Owner == 'Agnes'
    assert (t3.Done, t3.Id) == (False, None)

if __name__ == '__main__':
    t1 = task() # uses defaults
    t2 = task('Learn Python', 'Ethel')
