class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self, count=10):
        if self.head is None:
            print("The list is empty.")
            return
        
        current = self.head
        for _ in range(count):
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (circular)")

def main():
    circular_list = CircularSinglyLinkedList()
    
    values = [10, 20, 30, 40, 50]
    for value in values:
        circular_list.append(value)
    
    print("The circular singly linked list before insertion:")
    circular_list.display(count=10)
    
    new_value = 60
    circular_list.insert_at_end(new_value)
    
    print("The circular singly linked list after inserting at the end:")
    circular_list.display(count=10)

if __name__ == "__main__":
    main()
