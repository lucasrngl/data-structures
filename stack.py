# Stack implementation

class Stack:
    # Creating a stack
    def __init__(self):
        self.items = []
    
    # Check if stack is empty
    def check_empty(self):
        return len(self.items) == 0
    
    # Add an item into the stack
    def push(self, item):
        self.items.append(item)
    
    # Remove an item from the stack
    def pop(self):
        return self.items.pop()
    
    # Get the top element without removing it
    def peek(self):
        return self.items[len(self.items) - 1]

print("- Creating a stack")
stack = Stack()
print("- Stack is empty?", stack.check_empty())
print("- Adding 5 items into the stack")
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print("- Stack top before pop:", stack.peek())
print("- Stack pop method:", stack.pop())
print("- Stack top after pop:", stack.peek())