class Queue:
    def __init__(self, queue=None):
        if queue:
            self.queue = queue
        else:
            self.queue = []
    
    def print(self):
        print(self.queue)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False

    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.is_empty():
            return None
        first_element = self.queue[0]
        del self.queue[0]
        return first_element
