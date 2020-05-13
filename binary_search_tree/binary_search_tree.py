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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given node into the tree
    def insert(self, value):
        # Initialize a new node with the value parameter
        node = BSTNode(value)

        # In the case of a duplicate value, place to the right
        if self.value is node.value:  # (Do we need more logic here to not disrupt the tree?)
            self.right = node

        # GO RIGHT ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Case - new node value is greater than the one we're on:
        if self.value < node.value:
            # If the new node value is greater than the one we're on and the self.right is empty, we've found where to place the new node
            if self.right is None:
                # Reassign the right node of the point we're on
                self.right = node

            # if the given node is greater than the point we're on, but less than the point immediately to the right, we can infer it must go to the left of the node to the right
            elif self.right.value > node.value: 
                self.right.left = node

            else:
            # Otherwise if the right point it isn't empty or greater than the node, rerun the function recursively on the point immediately to the right
                return self.right.insert(value)

        # GO LEFT ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # Case - new node value is less than the one we're on:
        elif self.value > node.value:
            # If the new node value is less than the point we're on and self.left is empty, we've found where to place the new node
            if self.left is None:
                # Reassign the left node of the point we're on
                self.left = node

            # if the given node is less than the point we're on, but greater than the point immediately to the left, we can infer it must go to the right of the node to the left
            elif self.left.value < node.value: 
                self.left.right = node

            else:
            # Otherwise if the left point it isn't empty or less than the node, rerun the function recursively from the point immediately to the left
                return self.left.insert(value)




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
    def for_each(self, fn):
    # Set current to root of binary tree 
        current = self  
        stack = [] # initialize stack 
        # done = 0 
        
        while True: 
            
            # Reach the left most Node of the current Node 
            if current is not None: 
                
                # Place pointer to a tree node on the stack  
                # before traversing the node's left subtree 
                stack.append(current) 
            
                current = current.left  
    
            # BackTrack from the empty subtree and visit the Node 
            # at the top of the stack; however, if the stack is  
            # empty you are done 

            elif(stack): 
                current = stack.pop() 
                fn(current.value)
            
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
    
            else: 
                break


    # Part 2 -----------------------

    # Print all the nodes in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, value):
        pass

    # Print the node of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, value):
        pass

    # Print the node of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, value):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
