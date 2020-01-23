def test_method(*args):
    print(args[0])


if __name__ == '__main__':
    test_method('1', '2', 3, 4, { '5' }, [6])
