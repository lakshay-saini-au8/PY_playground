# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

def getNode(head, positionFromTail):
    if head is None:
        return
    if head.next is None:
        return head.data
    count = 0
    temp = head
    while temp is not None:
        count = count + 1
        temp = temp.next
    positionFromFront = count-positionFromTail
    test = head
    for i in range(positionFromFront-1):
        test = test.next
    return test.data

# second sol


def getNode(head, positionFromTail):
    if head is None:
        return
    if head.next is None:
        return head.data
    curr = head
    temp = head
    for i in range(positionFromTail):
        temp = temp.next

    while temp.next is not None:
        temp = temp.next
        curr = curr.next
    return curr.data
