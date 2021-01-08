"""
def abs(*args, **kwargs): # real signature unknown
    Return the absolute value of the argument.
"""
from operator import __abs__

sample = [
    10, - 10,
    10.5, - 10.5,
    0, 0.0,
]
for s in sample:
    print('{} => {}, {}'.format(s, abs(s), __abs__(s)))

"""
10    => 10
-10   => 10
10.5  => 10.5
-10.5 => 10.5
0     => 0
0.0   => 0.0
"""
