class TemperatureConverter:
    def __init__(self, conversion_factor):
        self.__conversion_factor = conversion_factor

    def convert_to_celsius(self, fahrenheit):
        return (fahrenheit - 32) * (5/9)

    def convert_to_fahrenheit(self, celsius):
        return celsius * (9/5) + 32

converter = TemperatureConverter(9/5)

celsius_temp = 30
fahrenheit_temp = converter.convert_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")

fahrenheit_temp = 80
celsius_temp = converter.convert_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")
