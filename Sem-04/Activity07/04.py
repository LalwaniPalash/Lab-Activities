class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None
        self.size = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        print(f"Enqueued {value} to queue.")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
        else:
            dequeued_value = self.front.value
            self.front = self.front.next
            if self.is_empty():
                self.rear = None
            self.size -= 1
            print(f"Dequeued {dequeued_value} from queue.")
            return dequeued_value
    
    def is_empty(self):
        return self.front is None
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            print("Queue elements from front to rear:")
            while current:
                print(current.value, end=" -> ")
                current = current.next
            print("None")

def main():
    queue = Queue()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    queue.display()
    
    queue.dequeue()
    queue.dequeue()
    
    queue.display()

if __name__ == "__main__":
    main()
