class TreeNode:
    def __init__(self, data):
        # Initialize a TreeNode with the given data and an empty list of children
        self.data = data  # Store the data in the node
        self.children = []

    def add_child(self, node):
        # Add a child node to the current node
        # Append the child node to the children list
        self.children.append(node)

    def traverse(self, level=0):
        # Print the data of the node and recursively print its children
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.traverse(level + 1)
