class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__ method called")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("__init__ method called")
        self.name = name

obj = MyClass("Example")
