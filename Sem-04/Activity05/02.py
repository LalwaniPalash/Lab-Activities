class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, value):
        if self.head is None:
            print("The list is empty. No node to delete.")
            return
        
        current = self.head
        prev = None
        
        if current.value == value:
            if current.next == self.head:
                self.head = None
            else:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            return
        
        while current.next != self.head and current.next.value != value:
            prev = current
            current = current.next
        
        if current.next.value == value:
            prev.next = current.next.next

    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        
        current = self.head
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (back to head)")

def main():
    circular_list = CircularLinkedList()
    
    print("Enter integer values to add to the circular linked list (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a value: ")
        if user_input.lower() == 'done':
            break
        try:
            value = int(user_input)
            circular_list.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer value.")
    
    print("The circular linked list:")
    circular_list.display()
    
    try:
        value_to_delete = int(input("Enter the value to delete: "))
        circular_list.delete(value_to_delete)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
    
    print("The circular linked list after deletion:")
    circular_list.display()

if __name__ == "__main__":
    main()
