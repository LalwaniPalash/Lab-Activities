class Temperature:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_to(self, new_unit):
        if self.unit == "Celsius" and new_unit == "Fahrenheit":
            self.value = (self.value * 9/5) + 32
            self.unit = "Fahrenheit"
        elif self.unit == "Fahrenheit" and new_unit == "Celsius":
            self.value = (self.value - 32) * 5/9
            self.unit = "Celsius"
        else:
            print("Conversion not supported")

temp1 = Temperature(25, "Celsius")
print("Initial temperature:", temp1.value, temp1.unit)

temp1.convert_to("Fahrenheit")
print("Converted temperature:", temp1.value, temp1.unit)
