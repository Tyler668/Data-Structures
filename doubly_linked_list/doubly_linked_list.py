"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):

        newNode = ListNode(value, None, None)
        self.length +=1
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode


            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        
        # what if the list is empty?
        if self.head:
            self.length -=1
            # we want to return the value at the current head 
            value = self.head.value
            # remove the value at the head 
            # update self.head

            if self.head.next:
                self.head = self.head.next
            # self.head.prev = None

            return value
        # what if it isn't empty?
        else:
            return None

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # self.length += 1
        # if self.tail is not None:
        #     current_tail = self.tail
        #     self.tail = ListNode(value, current_tail, None)
        #     # print('ADDING TO TAIL: ', self.tail.value, 'Prev = ', self.tail.prev.value, 'Next = ', self.tail.next)
        #     current_tail.next = self.tail
        newNode = ListNode(value, None, None)
        self.length +=1
        if self.tail == None:
            self.tail = newNode
            self.head = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode



    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.tail:
            return None

        
        current_tail = self.tail
        # self.delete(self.tail)
        self.tail = current_tail.prev
        if self.tail is None:
            return None

        self.tail.next = None

        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        current_head = self.head
        self.head = node
        self.head.prev = None
        self.head.next = current_head
        current_head.prev = self.head
        # if node is not self.head:
        #     current_head = self.head
        #     self.head.insert_before(node)
        #     node.next = current_head


        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.tail:
            return

        # if node.prev:
        #     node.prev.next = node.next
        # node.next.prev = node.prev

        self.delete(node)
        self.add_to_tail(node.value)

        # current_tail = self.tail
        # self.tail = node
        # node.next = None
        # node.prev = current_tail
        # current_tail.next = self.tail
        



    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # If node doesn't exist, return
        # if not self.exists(node.value):
        #     return 

        # Node exists

        self.length -= 1

        # Node is the only item in list
        if self.head is self.tail:
            self.head = None
            self.tail = None

        # Node is head
        elif node is self.head:
            self.head = self.head.next
            node.delete()

        # Node is tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()

        # Node is between head and tail
        else:
            node.delete()
       


        
    """Returns the highest value currently in the list"""
    def get_max(self):
        highest = self.head
        iterator = self.head
        
        while (iterator != None):
            if iterator.value > highest.value:
                highest = iterator
                
            iterator = iterator.next

        return highest.value

   