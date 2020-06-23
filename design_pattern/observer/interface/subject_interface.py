from abc import ABCMeta, abstractmethod

from design_pattern.observer.interface.observer_interface import Observer


class Subject(metaclass = ABCMeta):

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass
