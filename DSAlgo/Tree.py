class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Order:
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def search(self, root, key):
        if root.data is key:
            print("Found")
            return
        self.search(root.left)
        self.search(root.right)

    def height(self, root):
        if root is None:
            return 0
        left_tree = self.height(root.left)
        right_tree = self.height(root.right)
        return max(left_tree, right_tree) + 1
