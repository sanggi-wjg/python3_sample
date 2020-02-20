def raise_exception():
    raise TypeError('Test Except')


if __name__ == '__main__':

    try:
        raise_exception()

    except (Exception, TypeError) as e:
        print(e.args)
