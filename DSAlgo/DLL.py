class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # insert at start
    def insert_at_start(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert_at_end(self, data):
        currentNode = self.head
        newNode = Node(data)
        if currentNode is None:
            self.head = newNode
            return
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def traversal(self):
        currentNode = self.head
        while currentNode != None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next


dll = DoubleLinkedList()
dll.insert_at_start("start")
dll.insert_at_end("end")
dll.traversal()
