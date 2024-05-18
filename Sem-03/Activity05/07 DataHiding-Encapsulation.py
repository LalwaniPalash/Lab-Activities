class SecureData:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, int) and value >= 0:
            self.__value = value
        else:
            print("Invalid value. Must be a non-negative integer.")

data = SecureData(10)
print(data.get_value())

data.set_value(20)
print(data.get_value())

data.set_value(-5)
print(data.get_value())
