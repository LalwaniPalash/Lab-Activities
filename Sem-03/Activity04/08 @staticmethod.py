class MyClass:
    def instance_method(self, x, y):
        return x + y

    @staticmethod
    def static_method(x, y):
        return x + y

obj = MyClass()

print(obj.instance_method(3, 4))

print(MyClass.static_method(3, 4))

'''
In this example, instance_method is an existing instance method that depends on the instance (self) of the class. By adding the @staticmethod decorator above it, we convert it into a static method named static_method. This means the method no longer requires an instance of the class to be called; it can be called directly from the class itself.
'''
