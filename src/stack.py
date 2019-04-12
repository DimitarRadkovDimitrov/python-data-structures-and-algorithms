class Stack:
    def __init__(self, stack=None):
        if stack:
            self.stack = stack
        else:
            self.stack = []

    def print(self):
        print(self.stack)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
