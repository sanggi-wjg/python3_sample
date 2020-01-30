from abc import ABCMeta, abstractmethod


class TurkeyInterface(metaclass = ABCMeta):

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass
