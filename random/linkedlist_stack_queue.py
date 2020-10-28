class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


'''
take input in one line and end your list with -1 where you want to stop

1 2 3 4 5 6 7
'''


def createLinkedList():
    '''
    Input: 1 4 2 5 3 6 4 7 -1
    '''
    # getting data to insert inside list
    inputList = list(map(int, input().split()))
    head = None
    for currData in inputList:
        # checking for the end of the list
        if currData == -1:
            break
        newNode = Node(currData)
        # checking for first node or node
        if head is None:
            head = newNode
        else:
            currNode = head
            while currNode.next is not None:
                currNode = currNode.next
            currNode.next = newNode

    return head


def printLinkedList(head):
    '''
    Input: 1 4 2 5 3 6 4 7 -1
    Output: 1 -> 4 -> 2 -> 5 -> 3 -> 6 -> 4 -> 7 -> None
    '''
    currNode = head
    # checking till end node
    while currNode is not None:
        print(currNode.data, end=" -> ")
        currNode = currNode.next
    print("None")


def length(head):
    currNode = head
    count = 0
    while currNode is not None:
        count += 1
        currNode = currNode.next
    return count


def insert_after_i(head, i, data):
    '''
    to insert and element after ith position index start from 0
    '''
    currNode = head
    count = 0
    while count < i and (currNode.next is not None):
        currNode = currNode.next
        count += 1

    newNode = Node(data)
    newNode.next = currNode.next
    currNode.next = newNode


def reverse(head):
    if head is None or head.next is None:
        return head

    smallHead = reverse(head.next)
    currNode = smallHead
    while currNode.next is not None:
        currNode = currNode.next
    currNode.next = head
    head.next = None

    return smallHead


# head = createLinkedList()
# print(length(head))
# printLinkedList(head)
# head = reverse(head)
# # insert_after_i(head, 2, "second")
# printLinkedList(head)


'''
Stack
'''


class Stack:
    def __ini__(self, data):
        self.__data = []

    def push(self, data):
        self.__data.append(data)

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.__data.pop()

    def top(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.__data[-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False


'''
Queue

'''


class Queue:
    def __ini__(self, data):
        self.__data = []
        self.front = 0
        self.count = 0

    def enqueue(self, data):
        self.count += 1
        self.__data.append(data)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            el = self.__data[self.front]
            self.front += 1
            self.count -= 1
            return el

    def brat(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.__data[0]

    def size(self):
        return self.count

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
