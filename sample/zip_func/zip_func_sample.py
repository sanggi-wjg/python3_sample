from itertools import zip_longest

a = [1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e']
c = ['A', 'B', 'C']

for x, y, z in zip(a, b, c):
    print(x, y, z)

# 1 a A
# 2 b B
# 3 c C

###################################################################################################

for x, y, z in zip_longest(a, b, c):
    print(x, y, z)
    print((x, y, z))
    print([x, y, z])
# 1 a A
# (1, 'a', 'A')
# [1, 'a', 'A']
# 2 b B
# (2, 'b', 'B')
# [2, 'b', 'B']
# 3 c C
# (3, 'c', 'C')
# [3, 'c', 'C']
# 4 d None
# (4, 'd', None)
# [4, 'd', None]
# 5 e None
# (5, 'e', None)
# [5, 'e', None]
# 6 None None
# (6, None, None)
# [6, None, None]
# 7 None None
# (7, None, None)
# [7, None, None]
