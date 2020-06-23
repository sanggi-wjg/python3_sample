from time import sleep


class SampleClass(object):

    def show(self, value):
        print('Current temperature ', value)


class Data(object):
    _instance = None

    def __init__(self):
        self._weather = 1

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        self._weather = self._weather + value


if __name__ == '__main__':
    sample_class = SampleClass()
    data = Data()

    while True:
        sample_class.show(data.weather)
        data.weather = 1
        sleep(2)
