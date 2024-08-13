class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack: 
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self, data) -> None:
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1

    def pop(self) -> int:
        if self.top is None:
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    def sort_with_additional_stack(self) -> None:
        s = Stack()
        while self.top is not None:
            temp = self.pop()
            while s.top is not None and s.top.data < temp:
                self.push(s.pop())
            s.push(temp)
        while s.top is not None:
            self.push(s.pop())
    
    def sort_without_additional_stack(self) -> None:
        current = self.top
        while current is not None:
            next = current.next
            while next is not None:
                if current.data < next.data:
                    current.data, next.data = next.data, current.data
                next = next.next
            current = current.next
    
    def show(self) -> None:
        current = self.top
        while current is not None:
            print(current.data, end=" | ")
            current = current.next
        print("END")

def main() -> None:
    stack = Stack()

    stack.push(5)
    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(4)
    
    stack.show()
    print("Sorting...")
    stack.sort_with_additional_stack()
    print("Sorted:")
    stack.show()

if __name__ == "__main__":
    main()
