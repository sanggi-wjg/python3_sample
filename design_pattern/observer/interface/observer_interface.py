from abc import ABCMeta, abstractmethod


class Observer(metaclass = ABCMeta):

    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass
