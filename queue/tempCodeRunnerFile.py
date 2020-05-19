class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value) # How are these the same on stacks and queues
        return value

    def dequeue(self):
        if len(self) > 0:
            front = self.storage[0]
            self.storage.remove(front)
            return front
        else:
            return None

Linked list
