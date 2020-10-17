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


def largestData(root):
    if root == None:
        return 0
    leftLargest = largestData(root.left)
    rightLargest = largestData(root.right)
    return max(root.data, leftLargest, rightLargest)


def height(root):
    if root is None:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return max(leftHeight, rightHeight)+1


def numLeafNodes(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    leftTree = numLeafNodes(root.left)
    rightTree = numLeafNodes(root.right)
    return leftTree + rightTree


root = treeInput()
print(noofNode(root))
print(largestData(root))
print(height(root))
print(numLeafNodes(root))
printTree(root)
