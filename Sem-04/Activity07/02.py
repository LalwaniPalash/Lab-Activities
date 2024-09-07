class Queue:
    def __init__(self, capacity):
        self.capacity = capacity 
        self.queue = []          
        self.front = 0           
        self.rear = 0            
        self.size = 0            
    
    def enqueue(self, value):
        if self.is_overflow():
            print("Queue Overflow! Cannot enqueue the element.")
        else:
            self.queue.append(value)
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1
            print(f"Enqueued {value} to queue.")
    
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            print(f"Dequeued {value} from queue.")
            return value
    
    def is_empty(self):
        return self.size == 0
    
    def is_overflow(self):
        return self.size == self.capacity
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements from front to rear:")
            for i in range(self.size):
                index = (self.front + i) % self.capacity
                print(self.queue[index], end=" ")
            print()

def main():
    capacity = 5 
    queue = Queue(capacity)
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    
    queue.display()
    
    queue.dequeue()
    queue.dequeue()
    
    queue.display()

if __name__ == "__main__":
    main()
