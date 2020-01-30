from abc import ABCMeta, abstractmethod


class DuckInterface(metaclass = ABCMeta):

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass
