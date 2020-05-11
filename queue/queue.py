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

# Linked list



class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self, node = None):
        # first node in the list 
        self.head = node
        self.tail = node

        self.length = 0
    
    def __len__(self):
        return self.length

    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        self.length += 1
        # what if the list is empty? 
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)

    def remove_from_head(self):
        # what if the list is empty?
        if self.length > 0:
            self.length -= 1
        
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_end(value) # How are these the same on stacks and queues
        return value

    def dequeue(self):
        return self.storage.remove_from_head()


# 3.
# The difference between linked lists and array methods are that the array methods are already built in parts of the storage list. 
# We can use these instead of writing out our own in a linked list class, and we can reference indeces of the array whereas in linked
# lists we cannot.