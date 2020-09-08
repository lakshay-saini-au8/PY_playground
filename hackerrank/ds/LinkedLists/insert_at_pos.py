# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    currentNode = head
    for _ in range(position-1):
        currentNode = currentNode.next

    newNode = SinglyLinkedListNode(data)
    newNode.next = currentNode.next
    currentNode.next = newNode
    return head
