from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

