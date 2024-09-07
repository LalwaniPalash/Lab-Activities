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

    def search_value(self, target_value):
        current = self.head
        position = 0
        
        while current:
            if current.value == target_value:
                return position
            current = current.next
            position += 1
        
        return -1 

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
    
    print("The linked list:")
    linked_list.display()
    
    try:
        target_value = int(input("Enter the value to search for: "))
        position = linked_list.search_value(target_value)
        if position == -1:
            print("Value not found in the list.")
        else:
            print(f"Value found at position: {position}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

if __name__ == "__main__":
    main()
