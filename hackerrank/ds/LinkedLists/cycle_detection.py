# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

def has_cycle(head):

    if head is None:
        return 0
    if head.next is None:
        return 0
    slow_ptr = head
    fast_ptr = head
    while fast_ptr is not None:
        if fast_ptr.next is None:
            return 0

        fast_ptr = fast_ptr.next.next
        if slow_ptr == fast_ptr:
            return 1
        slow_ptr = slow_ptr.next
    return 0
