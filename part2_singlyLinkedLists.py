class Node:
    def __init__(self, data):
        # Initialize a Node with the given data and a pointer to the next node
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # Initialize an empty Singly Linked List with a head pointer

        self.head = None

    def insert(self, data):
        # Insert a new node with the given data at the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        # Delete the first node containing the specified key
        current = self.head  # Start from the head of the list
        previous = None

        # Traverse the list to find the node to delete
        while current is not None and current.data != key:
            previous = current
            current = current.next

        # If the key was not found, return False
        if current is None:
            return False

        # If the node to delete is the head
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        return True

    def traverse(self):
        # Print the data in each node from head to end of the list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
