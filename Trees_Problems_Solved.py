## TREES SOLUTIONS:

## Setting up the Class for the problem. 

class BST:
   # Define The class.

    class Node:
        # Each node of the BST will have values and links to the 
        # left and right sub-tree. 

        def __init__(self, data):
           # Initialize the node.

            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # Initialize an empty BST.

        self.root = None

    def insert(self, data):
        # Starter function to insert.
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        # This is the function that will look for an empty spot for your value
        # usuing recursion. 

        if data < node.data:
            # The value should go on the left.
            if node.left is None:
                # If there's space put it here. 
                node.left = BST.Node(data)
            else:
                # Doesn't fit there, keep going.  
                # Call _insert recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The value should go on the right.
            if node.right is None:
                # If there's space put it here. 
                node.right = BST.Node(data)
            else:
                # Doesn't fit there, keep going. 
                # Call _insert recursively on the right sub-tree.
                self._insert(data, node.right)

    ## Class set up ends here. (We need a BST with values in it to Traverse) 
    # Take a look at the Reverse Function here: 



    def __reversed__(self):
        # Initialize the Travers Backward Function

        yield from self._traverse_backward(self.root)  # Start at the root

    # Take a look at these functions, compare them to the Traverse Forward 
    # Functions in the examples Above Insert your code here to make the function traverse the BST backwards.
    def _traverse_backward(self, node):
        # FINISHED CODE HERE: 
        
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left) 


    ## BONUS PROBLEM SOLUTION:

    def __contains__(self, data):
        # Initialization of contains function. 

        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        # Write code to search through and see if a value is within our BST.

        # FINISHED CODE HERE:
        
        # Base Case: If we Find it, return it! 
        if data == node.data:
            return True
        
        if data < node.data:
            # We can reuse the Traverse Code to search for our value.
            if node.left is None:
                # We found an empty spot it's not there, return False.
                return False
            else:
                # Recurse like normal if we need to keep looking.
                return self._contains(data, node.left)
        else:
           # We can reuse the Traverse Code to search for our value.
            if node.right is None:
                # We found an empty spot it's not there, return False.
                return False 
            else:
                # Recurse like normal if we need to keep looking. 
                return self._contains(data, node.right) 

# Tests: 
                
tree = BST()
tree.insert(25)
tree.insert(13)
tree.insert(18)
tree.insert(4)
tree.insert(30)
tree.insert(27)
tree.insert(35)

for number in reversed(tree):
    print(number)
    
print(27 in tree) # Should print: True
print(95 in tree) # Should print: False    