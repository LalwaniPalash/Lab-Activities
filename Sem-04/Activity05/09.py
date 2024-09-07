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

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index 
            current = current.next
            index += 1
        return -1 

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
        target = int(input("Enter the value to search for: "))
        position = doubly_linked_list.search(target)
        if position != -1:
            print(f"Value {target} found at position {position}.")
        else:
            print(f"Value {target} not found in the list.")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
