from design_pattern.observer.interface.display_interface import Display
from design_pattern.observer.interface.observer_interface import Observer
from design_pattern.observer.interface.subject_interface import Subject


class HumidityDisplay(Observer, Display):
    humidity = None
    weather_data = None

    def __init__(self, subject: Subject):
        self.weather_data = subject
        self.weather_data.register_observer(self)

    def update(self, temperature: float, humidity: float, pressure: float):
        self.humidity = humidity
        self.display()

    def display(self):
        print('Current humidity is [{}]'.format(self.humidity))
