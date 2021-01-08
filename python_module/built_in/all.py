"""
def all(*args, **kwargs): # real signature unknown
    Return True if bool(x) is True for all values x in the iterable.

    If the iterable is empty, return True.
    pass
"""

sample = [
    [],
    [0],
    ['0'],
    [1],
    ['1'],
    [0, 1, 2],
    [1, 2, 3],
    [-0],
    [-1],
    [True],
    [False],
]

for s in sample:
    print(s, '=>', all(s))
