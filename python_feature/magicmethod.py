from typing import Any


class MagicClass:

    def __new__(cls, x, y, *args, **kwargs) -> Any:
        """
        __init__() 전에 호출이 된다.
        __init__() 으로 initialized 된 object 를 return 한다
        """
        print("__new__ x:{}\t y:{}\t args:{}\t kwargs:{}\t".format(x, y, args, kwargs))
        return super().__new__(cls)

    def __init__(self, x, y, *args, **kwargs):
        print("__init__ x:{}\t y:{}\t args:{}\t kwargs:{}\t".format(x, y, args, kwargs))
        self.x = x
        self.y = y
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        print("__del__")

    def __repr__(self) -> str:
        return "__repr__ x:{}\t y:{}\t args:{}\t kwargs:{}\t".format(self.x, self.y, self.args, self.kwargs)

    def __str__(self) -> str:
        return "__str__ x:{}\t y:{}\t args:{}\t kwargs:{}\t".format(self.x, self.y, self.args, self.kwargs)

    def __add__(self, other):
        return self.x + self.y + other

    def __mul__(self, other):
        return self.x * self.y * other

    def replace_method(self):
        print('replace_method')

    def __getattr__(self, item):
        # print('__getattr__', item)
        # return self.replace_method()
        return self.item


_MagicClass = MagicClass(5, 10, 'test', keyword = 'abc')
print(_MagicClass)
print(_MagicClass.__repr__())
print(_MagicClass.__str__())
print(_MagicClass + 2)
print(_MagicClass * 2)
print(getattr(_MagicClass, 'x'))
print(_MagicClass.test())

del _MagicClass
