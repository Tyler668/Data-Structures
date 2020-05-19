


"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!

"""


from singly_linked_list import LinkedList


# ARRAY

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value) # How are these the same on stacks and queues
#         return value

#     def dequeue(self):
#         if len(self) > 0:
#             front = self.storage[0]
#             self.storage.remove(front)
#             return front
#         else:
#             return None


# LINKED LIST

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()


# 3.
# The difference between linked lists and array methods are that the array methods are already built in parts of the storage list. 
# We can use these instead of writing out our own in a linked list class, and we can reference indeces of the array whereas in linked
# lists we cannot.