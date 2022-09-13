# Queue implementation

# Queue complexity: O(1) - enqueue and dequeue methods in queue are always constant

class Queue:

    # Creating a queue
    def __init__(self):
        self.queue = []

    # Check if queue is empty
    def check_empty(self):
        return len(self.queue) == 0
    
    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # Get the front element without removing it
    def peek(self):
        return self.queue[0]

print("- Creating a queue")
queue = Queue()
print("- Queue is empty?", queue.check_empty())
print("- Adding 5 items into the queue")
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
print("- Queue front before dequeue:", queue.peek())
print("- Queue dequeue method:", queue.dequeue())
print("- Queue front after dequeue:", queue.peek())