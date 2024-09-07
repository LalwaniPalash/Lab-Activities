class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def push(self, value):
        if self.is_overflow():
            print("Stack Overflow! Cannot push the element.")
        else:
            self.stack.append(value)
            print(f"Pushed {value} to stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        else:
            value = self.stack.pop()
            print(f"Popped {value} from stack.")
            return value
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_overflow(self):
        return len(self.stack) >= self.capacity
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements from top to bottom:")
            for item in reversed(self.stack):
                print(item)

def main():
    capacity = 5
    stack = Stack(capacity)
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    
    stack.display()
    
    stack.pop()
    stack.pop()
    
    stack.display()

if __name__ == "__main__":
    main()
