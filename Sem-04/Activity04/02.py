class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
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

    def traverse_and_print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

def main():
    linked_list = SinglyLinkedList()
    
    print("Enter integer values to add to the linked list (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            linked_list.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("Traversing and printing the linked list:")
    linked_list.traverse_and_print()

if __name__ == "__main__":
    main()
