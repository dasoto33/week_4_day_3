from Node import Node

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        curr = self.root
        while True:
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

    def inorder_traversal(self, node, sorted_list):
        if node:
            self.inorder_traversal(node.left, sorted_list)
            sorted_list.append(node.value)
            self.inorder_traversal(node.right, sorted_list)



