from itertools import permutations

import numpy as np


def find_nearest(data, find_value):
    data = np.asarray(data)
    idx = (np.abs(data - find_value)).argmin()
    return data[idx]


if __name__ == '__main__':
    CARDS = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
    HOPE_FIND_VALUE = 500

    permuted_data = permutations(CARDS, 3)
    permuted_data = set(map(lambda x: tuple(sorted(x)), permuted_data))

    psum = []
    for p in permuted_data:
        psum.append(p[0] + p[1] + p[2])

    print(find_nearest(psum, HOPE_FIND_VALUE))
