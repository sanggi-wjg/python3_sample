from datetime import datetime


def decorate_function(func):
    def decorated():
        print(datetime.now())
        func()

    return decorated


@decorate_function
def main_function_1():
    print("Main function 111111 Start")


if __name__ == '__main__':
    # main_function_1()

    a = { 1: 2 }
    b = { 3: 4 }
    a.update(b)
    print(a)
