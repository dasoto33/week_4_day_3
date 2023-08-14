from linkedlist import LinkedList
from BST import BST

def create_sorted_linked_list(unsorted_list):
    bst = BST()
    linked_list = LinkedList()

    # Create BST
    for item in unsorted_list:
        bst.insert(item)

    # In-order traversal and add to linked list
    sorted_list = []
    bst.inorder_traversal(bst.root, sorted_list)
    for item in sorted_list:
        linked_list.append(item)

    return linked_list

if __name__ == "__main__":
    unsorted_list = [5, 2, 8, 1, 3, 7, 9]
    sorted_linked_list = create_sorted_linked_list(unsorted_list)
    sorted_linked_list.display()