if __name__ == '__main__':
    each = dict()
    keys = ['test', 'test_1', 'test_2']

    for k in keys:
        each.__setitem__(k, { 'a': 1, 'b': 2 })

    print(each.get('test3'))

    print(each)

    print(
        {
            'test'  : {
                'a': 1,
                'b': 2
            },
            'test_1': {
                'a': 1,
                'b': 2
            },
            'test_2': {
                'a': 1,
                'b': 2
            }
        }
    )
