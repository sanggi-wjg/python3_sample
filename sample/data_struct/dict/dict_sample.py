if __name__ == '__main__':
    each = dict()
    keys = ['test_1', 'test_2', 'test_3']

    for k in keys:
        each.__setitem__(k, { 'a': 1, 'b': 2 })

    print(each.get('test_3'))
    print(each)

