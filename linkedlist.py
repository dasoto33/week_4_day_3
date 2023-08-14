from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

# method to add node
    def append(self, value):
        new_node = Node(value) #create instance of Node class with value presented
        if not self.head: # check to see if list is empty and add node as head of list if it is
            self.head = new_node 
            return
        curr = self.head # assigns curr as a traversal pointer to head of list
        while curr.next:
            curr = curr.next # traverses the list
        curr.next = new_node # adds new node to end of list

# method to display node
# basically a create a print function 
    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ") 
            curr = curr.next
        print("None")

