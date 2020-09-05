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

    # method to insert a node after a given node
    def insert_at_pos(self, pos, data):
        if pos is None:
            print("Given position doesn't exist")
        newNode = Node(data)
        newNode.next = pos.next
        pos.next = newNode

    # method to delete a node from begning
    def delete_from_beg(self):
        currentNode = self.head
        if currentNode is None:
            print(f"List is already empyt")
            return
        self.head = currentNode.next
        currentNode.next = None

    # method to delete a node from end
    def delete_from_end(self):
        currentNode = self.head
        if currentNode is None:
            print(f"List is already empyt")
            return
        while(currentNode.next.next is not None):
            currentNode = currentNode.next
        currentNode.next = None

    # method to delete a key
    def delete_key(self, key):
        currentNode = self.head

        while(currentNode.next.data != key):
            currentNode = currentNode.next
            if currentNode.next is None:
                print(f"this is {key}  not present")
                return
        temp = currentNode.next
        currentNode.next = currentNode.next.next
        temp.next = None

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
ll.insert_at_pos(ll.head.next, 70)
ll.delete_key(110)
ll.delete_from_beg()
ll.delete_from_end()

ll.traverse()
