class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def display(self, count=10):
        if self.head is None:
            print("The list is empty.")
            return
        
        current = self.head
        for _ in range(count): 
            print(current.value, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("... (circular)")

def main():
    cdll = CircularDoublyLinkedList()
    
    values = [10, 20, 30, 40, 50]
    for value in values:
        cdll.append(value)
    
    print("The circular doubly linked list before appending:")
    cdll.display(count=10)
    
    new_value = 60
    cdll.append(new_value)
    
    print("The circular doubly linked list after appending a new node:")
    cdll.display(count=10)

if __name__ == "__main__":
    main()
