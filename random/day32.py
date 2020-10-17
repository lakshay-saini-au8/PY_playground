class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(root):
    if root is None:
        return
    print(root.data, end=":")
    if root.left is not None:
        print("L->", root.left.data, end=",")
    if root.right is not None:
        print("R->", root.right.data, end=" ")
    print()
    printTree(root.left)
    printTree(root.right)


def treeInput():
    rootData = int(input())
    if rootData == -1:
        return None
    root = Node(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


def noofNode(root):
    if root is None:
        return 0
    left = noofNode(root.left)
    right = noofNode(root.right)
    return left+right+1


btn1 = Node(1)
btn2 = Node(2)
btn3 = Node(3)
btn4 = Node(4)
btn5 = Node(5)

btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5
printTree(btn1)
print(noofNode(btn1))
