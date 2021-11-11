
"""
>>> add(5,2)
7

>>> add(10, 10)
19
"""


def add(a, b):
    return a + b



if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Running this command: py -m doctest -v doctests.py
# produces the following output:

"""
Trying:
    add(5,2)
Expecting:
    7
ok
Trying:
    add(10, 10)
Expecting:
    19
**********************************************************************      
File "C:/Users/keego/Documents/Repos/pdx_code/Class_Raven/1 Python/demo/doct
ests.py", line 6, in doctests
Failed example:
    add(10, 10)
Expected:
    19
Got:
    20
1 items had no tests:
    doctests.add
**********************************************************************      
1 items had failures:
   1 of   2 in doctests
2 tests in 2 items.
1 passed and 1 failed.
***Test Failed*** 1 failures.
"""