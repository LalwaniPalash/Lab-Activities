class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def convert_to_circular(self):
        if self.head is None:
            print("The list is empty. Cannot convert to a circular doubly linked list.")
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = self.head
        self.head.prev = last

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
    doubly_linked_list = DoublyLinkedList()
    
    print("Enter integer values to add to the doubly linked list (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            doubly_linked_list.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("The doubly linked list:")
    doubly_linked_list.display()
    
    doubly_linked_list.convert_to_circular()
    
    print("The circular doubly linked list:")
    doubly_linked_list.display(count=15) 

if __name__ == "__main__":
    main()
