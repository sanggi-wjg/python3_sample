from dataclasses import dataclass


def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func


def decorator_func(origin_func):
    def wrapper_func():
        return origin_func()

    return wrapper_func


def display():
    print('display Method...')


if __name__ == '__main__':
    # print(outer_func('Hello'))
    # outer_func('Hello')()

    # deco_display = decorator_func(display)
    # deco_display()

    temp = dataclass
    temp.abc = '123'

    print(temp)
    print(temp.abc)
