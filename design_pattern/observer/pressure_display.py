from design_pattern.observer.interface.display_interface import Display
from design_pattern.observer.interface.observer_interface import Observer
from design_pattern.observer.interface.subject_interface import Subject


class PressureDisplay(Observer, Display):
    pressure = None
    weather_data = None

    def __init__(self, subject: Subject):
        self.weather_data = subject
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.pressure = pressure
        self.display()

    def display(self):
        print('Current pressure is [{}]'.format(self.pressure))
