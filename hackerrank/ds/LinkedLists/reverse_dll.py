# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem
def reverse(head):
    temp = None
    current = head

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if temp is not None:
        head = temp.prev
    return head
