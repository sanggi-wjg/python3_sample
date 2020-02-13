import collections

if __name__ == '__main__':
    print('Regular dictionary:')
    d = { }
    print(type(d), d)
    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    print(type(d), d)

    for k, v in d.items():
        print(k, v)

    print('\nOrderedDict:')
    orderdict = collections.OrderedDict()
    print(type(orderdict), orderdict)
    orderdict['a'] = 'A'
    orderdict['b'] = 'B'
    orderdict['c'] = 'C'
    print(type(orderdict), orderdict)

    for k, v in orderdict.items():
        print(k, v)
