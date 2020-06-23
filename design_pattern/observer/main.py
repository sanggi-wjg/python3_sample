from design_pattern.observer.humidity_display import HumidityDisplay
from design_pattern.observer.pressure_display import PressureDisplay
from design_pattern.observer.temperature_display import TemperatureDisplay
from design_pattern.observer.weather_data import WeatherData

weather_data = WeatherData()
temperature_display = TemperatureDisplay(weather_data)
humidity_display = HumidityDisplay(weather_data)
pressure_display = PressureDisplay(weather_data)

print('\n[0] Set Weather Data 30 / 65 / 30.4')
weather_data.set_weather_data(30, 65, 30.4)
print('\n[1] Set Weather Data 35 / 80 / 35.4')
weather_data.set_weather_data(35, 80, 35.4)
