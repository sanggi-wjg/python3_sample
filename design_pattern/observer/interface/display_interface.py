from abc import ABCMeta, abstractmethod


class Display(metaclass = ABCMeta):

    @abstractmethod
    def display(self):
        pass
