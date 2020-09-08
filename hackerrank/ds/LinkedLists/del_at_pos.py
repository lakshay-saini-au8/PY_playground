# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    currentNode = head
    if position == 0:
        head = head.next
        currentNode.next = None
        return head
    for _ in range(position - 1):
        currentNode = currentNode.next
    if currentNode is not None:
        currentNode.next = currentNode.next.next

    return head
