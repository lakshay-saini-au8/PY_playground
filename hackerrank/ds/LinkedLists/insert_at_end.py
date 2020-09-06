# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertNodeAtTail(head, data):
    temp = head
    newNode = SinglyLinkedListNode(data)
    if temp == None:
        return newNode
    while(temp.next != None):
        temp = temp.next
    temp.next = newNode

    return head
