from design_pattern.observer.humidity_display import HumidityDisplay
from design_pattern.observer.temperature_display import TemperatureDisplay
from design_pattern.observer.weather_data import WeatherData

weather_data = WeatherData()
temperature_display = TemperatureDisplay(weather_data)
humidity_display = HumidityDisplay(weather_data)

weather_data.set_weather_data(30, 65, 30.4)
