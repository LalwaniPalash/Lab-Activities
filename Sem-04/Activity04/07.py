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

    def delete_last_node(self):
        if self.head is None:
            print("The list is empty. No node to delete.")
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next and current.next.next:
            current = current.next
        
        current.next = None

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
            linked_list.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("The linked list before deletion:")
    linked_list.display()
    
    linked_list.delete_last_node()
    
    print("The linked list after deleting the last node:")
    linked_list.display()

if __name__ == "__main__":
    main()
