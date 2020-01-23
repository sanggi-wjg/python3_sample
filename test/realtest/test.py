from datetime import datetime


def test_method():
    dep_test_method()


def dep_test_method():
    print(__name__)


def print_method(msg, *args):
    print(msg, *args)


def escape_in_code(code: str = '') -> str:
    if code == '':
        return code

    result = code.replace('.', '')
    result = result.replace('-', '')
    result = result.replace(' ', '')

    return result


class TestClass:

    def print_cls_name(self):
        print(self.__class__.__name__)


if __name__ == '__main__':
    # test_method()
    # print_method('123123213', 123, '123')
    # _TestClass = TestClass()
    # _TestClass.print_cls_name()
    # print(escape_in_code('1-2 3.123'))

    stdClass = object
    stdClass.__setattr__('temp', '123')
    print(stdClass.__getattribute__('temp'))
