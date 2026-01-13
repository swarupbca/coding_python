class node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


def insert(root, value):
    if root is None:
        return node(value)

    if value < root.data:
        root.left_node = insert(root.left_node, value)
    elif value > root.data:
        root.right_node = insert(root.right_node, value)

    return root


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
print(root)
