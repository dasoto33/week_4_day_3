from Node import Node

class BST:
    def __init__(self):
        self.root = None

# method inserts node into BST
    def insert(self, value):
        new_node = Node(value)
        if not self.root: # checks if tree is empty, if it is, value becomes root
            self.root = new_node
            return
        curr = self.root 
        while True: # loops checks for left child or right child and if it is greater than the current inputed value
            if value < curr.value: 
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right

# method to traverse the BST in order
    def inorder_traversal(self, node, sorted_list):
        if node:
            self.inorder_traversal(node.left, sorted_list) #traverses left of current node
            sorted_list.append(node.value) # appends current node to list
            self.inorder_traversal(node.right, sorted_list) # traverses right of current node



