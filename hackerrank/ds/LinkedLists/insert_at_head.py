# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

def insertNodeAtHead(llist, data):

    newNode = SinglyLinkedListNode(data)
    if llist is None:
        return newNode
    newNode.next = llist
    llist = newNode
    return llist
