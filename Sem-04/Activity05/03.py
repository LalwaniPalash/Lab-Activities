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

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if slow:
            return slow.value
        else:
            return None 

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
    
    middle_value = linked_list.find_middle()
    if middle_value is not None:
        print(f"The middle node value is: {middle_value}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
