"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given node into the tree
    def insert(self, value):
        # check if the incoming value is less than the current node's value 
        if value < self.value:
            # we know we need to go left 
            # how do we know when we need to recurse again, 
            # or when to stop? 
            if not self.left:
                # we can park our value here 
                self.left = BSTNode(value)
            else:
                # we can't park here 
                # keep searching 
                self.left.insert(value)
        else:
            # we know we need to go right 
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the node
    # False if it does not
    def contains(self, target):
        # When we start searching, self will be the root,
        # compare the targets against self

        # Criteria for returning false: we know we need to go in one direction
        # but there's nothing in that direction, end of tree with no results
        if target == self.value:
            return True

        if target < self.value: # ---> Go left
            # If we haven't found our node and it's smaller than the one we're on,
            # yet there is nothing to the left, it can't exist, return false
            if not self.left:
                return False

            return self.left.contains(target)
        if target > self.value: # ---> Go right
            # If we haven't found our node and it's larger than the one we're on,
            # yet there is nothing to the right, it can't exist, return false

            if not self.right:
                return False
                
            return self.right.contains(target)

    # Return the maximum node found in the tree
    def get_max(self):
        max = self
        temp = self

        while temp != None:
            max = temp
            temp = temp.right

        return max.value

    # Call the function `fn` on the node of each node
    # Highly epic recursive DFT for each
    #------------------------------------------------------
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)
    #------------------------------------------------------

    # Iterative depth first traversal
    # Set current to root of binary tree 
    def iter_depth_for_each(self, fn):
        stack = [] 

        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements 
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)




        # current = self  
        # stack = [] # initialize stack         
        # while True: 
        #     # Reach the left most Node of the current Node 
        #     if current is not None: 
                
        #         # Place pointer to a tree node on the stack  
        #         # before traversing the node's left subtree 
        #         stack.append(current) 
            
        #         current = current.left  
    
        #     # BackTrack from the empty subtree and visit the Node 
        #     # at the top of the stack; however, if the stack is  
        #     # empty you are done 

        #     elif(stack): 
        #         current = stack.pop() 
        #         fn(current.value)
            
        #         # We have visited the node and its left  
        #         # subtree. Now, it's right subtree's turn 
        #         current = current.right  
    
        #     else: 
        #         break



    # --------------------------------------------------------

    # Breadth - first
    def breadth_for_each(self, fn):
        queue = deque()

        # add the root node
        queue.append(self)

        # loop so long as the stack still has elements 
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            fn(current.value)

    # Part 2 -----------------------

    # Print all the nodes in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, value):
        arr = []
        value.for_each(lambda x: arr.append(x))
        arr.sort()
        for i in arr:
            print(f"{i}")


    # Print the node of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, value):
        value.breadth_for_each(lambda x: print(x))

    # Print the node of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, value):
        value.iter_depth_for_each(lambda x: print(x))
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



# bst = BSTNode(5)
# bst.insert(8)
# bst.insert(9)
# bst.insert(3)
# bst.insert(6)
# bst.insert(4)
# bst.insert(1)

# bst.dft_print(bst)