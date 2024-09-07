class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        print(f"Pushed {value} to stack.")
    
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Cannot pop from an empty stack.")
            return None
        else:
            popped_value = self.top.value
            self.top = self.top.next
            self.size -= 1
            print(f"Popped {popped_value} from stack.")
            return popped_value
    
    def is_empty(self):
        return self.top is None
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            current = self.top
            print("Stack elements from top to bottom:")
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

def main():
    stack = Stack()
    
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.display()
    
    stack.pop()
    stack.pop()
    
    stack.display()

if __name__ == "__main__":
    main()
