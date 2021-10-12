# good test strategy
# 1. come up with a plan
# 2. write tests, not code
# 3. write code
# 4. stop when tests pass

# using pytest

def test_pass():
    assert (1,2,3) == (1,2,3)

#def test_fail():
#    assert (1,2,3) == (3,2,1)

def test_sets():
    assert {1,2,3} == {3,2,1}