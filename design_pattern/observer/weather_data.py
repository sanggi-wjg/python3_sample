from design_pattern.observer.interface.observer_interface import Observer
from design_pattern.observer.interface.subject_interface import Subject


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def register_observer(self, observer: Observer):
        print(observer.__class__.__name__, ': registered')
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        print(observer.__class__.__name__, ': removed')
        self.observers.remove(observer)

    def notify_observers(self):
        for obs in self.observers:
            print(obs.__class__.__name__, ': notified')
            obs.update(self._temperature, self._humidity, self._pressure)

    @property
    def temperature(self):
        return self._temperature

    @property
    def humidity(self):
        return self._humidity

    @property
    def pressure(self):
        return self._pressure

    def measurements_changed(self):
        self.notify_observers()

    def set_weather_data(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()
