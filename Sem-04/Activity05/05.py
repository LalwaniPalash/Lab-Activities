class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

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
            doubly_linked_list.prepend(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("The doubly linked list:")
    doubly_linked_list.display()

if __name__ == "__main__":
    main()
