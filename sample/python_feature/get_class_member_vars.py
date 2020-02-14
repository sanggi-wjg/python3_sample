import inspect


class TargetClass:
    TYPE_A = 'A'
    TYPE_B = 2
    TYPE_C = ['c']

    def __init__(self):
        TYPE_D = 'd'
        TYPE_E = 5
        TYPE_F = ['f']


if __name__ == '__main__':
    # atrs = inspect.getmembers(TargetClass)
    # print(atrs)

    # vars = inspect.getmembers(TargetClass, lambda a: not (inspect.isroutine(a)))
    # print(vars)

    print(vars(TargetClass))
