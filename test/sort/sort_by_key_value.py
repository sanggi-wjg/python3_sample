def sort_by(numbers, byWhat):
    res = dict()

    for n in numbers:
        res.__setitem__(str(n), str(n)[0])

    print('origin : ', res)
    if byWhat == 'key':
        res = sorted(res.items(), key = lambda x: x[1], reverse = True)
    elif byWhat == 'value':
        res = sorted(res.items(), key = lambda x: x[0], reverse = True)
    print('sorted : ', res)


if __name__ == '__main__':
    sort_by([3, 33, 30, 34, 5, 9, 100, 110], 'key')
    sort_by([3, 33, 30, 34, 5, 9, 100, 110], 'value')
