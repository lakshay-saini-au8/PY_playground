# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
# sol1
# using an array
def reversePrint(head):
    result = []
    if head is None:
        return
    if head.next is None:
        print(head.data)
        return
    temp = head
    while temp is not None:
        result.append(temp.data)
        temp = temp.next
    result.reverse()
    for i in result:
        print(i)

# sol 2
# using recursion


def reversePrint(head):
    if head is None:
        return
    else:
        reversePrint(head.next)
        print(head.data)
