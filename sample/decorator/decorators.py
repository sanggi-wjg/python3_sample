from datetime import datetime


def decorate_function(func):
    def decorated():
        print(datetime.now())
        func()

    return decorated


@decorate_function
def main_function_1():
    print("Hello Python Decorator!")


if __name__ == '__main__':
    main_function_1()
