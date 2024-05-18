class ObjectComparator:
    def __init__(self, obj1, obj2):
        self.obj1 = obj1
        self.obj2 = obj2

    def compare_type(self):
        return type(self.obj1) == type(self.obj2)

    def compare_attributes(self):
        if not self.compare_type():
            return False
        return self.obj1.__dict__ == self.obj2.__dict__

    def compare_identity(self):
        return self.obj1 is self.obj2

class ExampleClass:
    def __init__(self, attribute):
        self.attribute = attribute

obj1 = ExampleClass(10)
obj2 = ExampleClass(10)
obj3 = obj1

comparator1 = ObjectComparator(obj1, obj2)
print("Same type:", comparator1.compare_type())
print("Same attributes:", comparator1.compare_attributes())
print("Same identity:", comparator1.compare_identity())

comparator2 = ObjectComparator(obj1, obj3)
print("Same type:", comparator2.compare_type())
print("Same attributes:", comparator2.compare_attributes())
print("Same identity:", comparator2.compare_identity())
