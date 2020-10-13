class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, pos, data):

    temp = pos
    pos = Node(data)
    return root


def inorder(root):

    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def search(root, key):
    if root.data is key:
        print("Found")
        return
    search(root.left)
    search(root.right)


def height(root):
    if root is None:
        return 0
    left_tree = height(root.left)
    right_tree = height(root.right)
    return max(left_tree, right_tree) + 1


root = Node(4)

insert(root, root.left, 5)
insert(root, root.right, 5)
inorder(root)
