class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def main():
    linked_list = SinglyLinkedList()
    
    print("Enter integer values to add to the linked list (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            linked_list.prepend(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("The linked list after insertion at the beginning:")
    linked_list.display()

if __name__ == "__main__":
    main()
