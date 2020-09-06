# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    temp = head
    if temp == None:
        print(temp)
        return
    while(temp != None):
        print(temp.data)
        temp = temp.next
