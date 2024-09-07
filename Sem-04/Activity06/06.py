class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
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

    def count_nodes(self):
        if self.head is None:
            return 0
        
        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def display(self, count=10):
        if self.head is None:
            print("The list is empty.")
            return
        
        current = self.head
        for _ in range(count):
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("... (circular)")

def main():
    circular_list = CircularSinglyLinkedList()
    
    values = [10, 20, 30, 40, 50]
    for value in values:
        circular_list.append(value)
    
    print("The circular singly linked list:")
    circular_list.display(count=10)
    
    num_nodes = circular_list.count_nodes()
    print(f"Number of nodes in the circular singly linked list: {num_nodes}")

if __name__ == "__main__":
    main()
