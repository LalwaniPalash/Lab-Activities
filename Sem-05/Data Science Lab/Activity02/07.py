import temperature_converter  # Import the temperature_converter module

def test_temperature_conversions():
    celsius = 25
    fahrenheit = temperature_converter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")

    fahrenheit = 77
    celsius = temperature_converter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")

if __name__ == "__main__":
    test_temperature_conversions()
