"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from singly_linked_list import LinkedList


# ARRAY

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value) # How are these the same on stacks and queues
#         return value

#     def pop(self):
#         if len(self) > 0:
#             toPop = self.storage[len(self) - 1]
#             self.storage.remove(self.storage[len(self) - 1])
#             return toPop

#         else:
#             return None


# LINKED LIST

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

# 3.
# The difference between linked lists and array methods are that the array methods are already built in parts of the storage list. 
# We can use these instead of writing out our own in a linked list class, and we can reference indeces of the array whereas in linked
# lists we cannot. Additionally when implementing linked lists with stacks, it seems we need to have an additional 'Remove from tail' 
# method in order to properly pop() in the way that is expected with a stack.