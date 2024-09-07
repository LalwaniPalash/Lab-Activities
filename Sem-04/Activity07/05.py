class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)
    
    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value, end=" ")
            self.in_order_traversal(node.right)
    
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=" ")

def main():
    tree = BinaryTree()
    
    values = [10, 5, 20, 3, 7, 15, 25]
    for value in values:
        tree.insert(value)
    
    print("In-Order Traversal:")
    tree.in_order_traversal(tree.root)
    print()
    
    print("Pre-Order Traversal:")
    tree.pre_order_traversal(tree.root)
    print()
    
    print("Post-Order Traversal:")
    tree.post_order_traversal(tree.root)
    print()

if __name__ == "__main__":
    main()
