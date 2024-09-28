class Stack:
    def __init__(self, size):
        # Initialize the Stack with a specified size and an empty list
        self.size = size
        self.stack = []

    def push(self, value):
        # Add a value to the top of the Stack if it is not full
        if len(self.stack) < self.size:
            self.stack.append(value)  # Append the value to the stack
        else:
            # Raise error if stack is full
            raise OverflowError("Stack is full.")

    def pop(self):
        # Remove and return the top value from the Stack if it is not empty
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the last value
        else:
            # Raise error if stack is empty
            raise IndexError("Stack is empty.")

    def peek(self):
        # Return the top value of the Stack without removing it
        if not self.is_empty():
            return self.stack[-1]  # Return the last value
        else:
            # Raise error if stack is empty
            raise IndexError("Stack is empty.")

    def is_empty(self):
        # Check if the Stack is empty
        return len(self.stack) == 0  # Return True if empty, False otherwise


class Queue:
    def __init__(self, size):
        # Initialize the Queue with a specified size and an empty list
        self.size = size
        self.queue = []

    def enqueue(self, value):
        # Add a value to the end of the Queue if it is not full
        if len(self.queue) < self.size:
            self.queue.append(value)  # Append the value to the queue
        else:
            # Raise error if queue is full
            raise OverflowError("Queue is full.")

    def dequeue(self):
        # Remove and return the front value from the Queue if it is not empty
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the first value
        else:
            # Raise error if queue is empty
            raise IndexError("Queue is empty.")

    def is_empty(self):
        # Check if the Queue is empty
        return len(self.queue) == 0  # Return True if empty, False otherwise
