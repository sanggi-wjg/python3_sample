from pprint import pprint

temp = [
    'BBBBBBBBWBWBW',
    'BBBBBBBBBWBWB',
    'BBBBBBBBWBWBW',
    'BBBBBBBBBWBWB',
    'BBBBBBBBWBWBW',
    'BBBBBBBBBWBWB',
    'BBBBBBBBWBWBW',
    'BBBBBBBBBWBWB',
    'WWWWWWWWWWBWB',
    'WWWWWWWWWWBWB'
]
temp = temp[0:8]
A = []
for t in temp:
    A.append(t[0:8])
pprint(A)

t = []
for a in A:
    t.append(list(a))
pprint(t)
