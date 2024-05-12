class MyClass:
    class_attribute = "class_attribute_value"

    def __init__(self):
        self.instance_attribute = "instance_attribute_value"

    def instance_method(self):
        pass

# Creating an instance of MyClass
obj = MyClass()

print("Using vars():")
print(vars(obj))  # Output: {'instance_attribute': 'instance_attribute_value'}

print("\nUsing dir():")
print(dir(obj))
