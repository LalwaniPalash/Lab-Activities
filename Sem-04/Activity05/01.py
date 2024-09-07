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

    def display(self):
        current = self.head
        while current:
            print(f"{current.value}", end=" <-> ")
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

if __name__ == "__main__":
    main()
