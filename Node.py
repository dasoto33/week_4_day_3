class Node:
    # takes in parameter (data) which will hod the node data
    def __init__(self, value):
        self.value = value # used to store the node data
        self.left = None
        self.right = None
        self.next = None # don't know what the next node will be, so set to None 