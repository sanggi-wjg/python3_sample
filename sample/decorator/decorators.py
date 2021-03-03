from datetime import datetime


def decorate_function(func):
    def decorated(temp):
        print(datetime.now())
        func(temp)

    return decorated


@decorate_function
def main_function_1(temp):
    print("Hello Python Decorator!")
    print(temp)


if __name__ == '__main__':
    temp = { 'a': 'b' }
    main_function_1(temp)
