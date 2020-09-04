class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # method to insert a node in starting
    def insert_at_start(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # method to insert a node in the end
    def insert_at_end(self, data):
        newNode = Node(data)
        currentNode = self.head
        if currentNode is None:
            newNode.next = self.head
            self.head = newNode
            return
        while(currentNode.next is not None):
            currentNode = currentNode.next
        currentNode.next = newNode

    def insert_at_pos(self, pos, data):
        if pos is None:
            print("Given position doesn't exist")

    # method to print the linked list

    def traverse(self):
        if self.head is None:
            print("Sorry linked list doesn't exist")
            return
        currentNode = self.head
        while(currentNode is not None):
            print(currentNode.data, end=" ")
            currentNode = currentNode.next


ll = LinkedList()
ll.insert_at_start(20)
ll.insert_at_start(30)
ll.insert_at_end(50)
ll.insert_at_end(40)
ll.traverse()
