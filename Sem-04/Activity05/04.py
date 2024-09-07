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

    def delete_at_position(self, position):
        if self.head is None:
            print("The list is empty. No node to delete.")
            return
        
        current = self.head
        
        if position == 0:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return
        
        index = 0
        while current and index < position:
            current = current.next
            index += 1
        
        if current is None:
            print("Position out of bounds.")
            return
        
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

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
    
    try:
        position = int(input("Enter the position of the node to delete (0-based index): "))
        doubly_linked_list.delete_at_position(position)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
    
    print("The doubly linked list after deletion:")
    doubly_linked_list.display()

if __name__ == "__main__":
    main()
