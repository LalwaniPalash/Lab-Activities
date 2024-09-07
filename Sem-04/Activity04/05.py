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

    def insert_at_position(self, value, position):
        new_node = Node(value)
        if position < 0:
            raise IndexError("Position must be a non-negative integer.")
        
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        current_position = 0
        
        while current and current_position < position - 1:
            current = current.next
            current_position += 1
        
        if current is None:
            raise IndexError("Position out of bounds.")
        
        new_node.next = current.next
        current.next = new_node

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
    
    print("The linked list before insertion:")
    linked_list.display()
    
    try:
        value = int(input("Enter the value to insert: "))
        position = int(input("Enter the position to insert at: "))
        linked_list.insert_at_position(value, position)
    except ValueError:
        print("Invalid input. Please enter integer values.")
    except IndexError as e:
        print(e)
    
    print("The linked list after insertion:")
    linked_list.display()

if __name__ == "__main__":
    main()
