# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
def mergeLists(head1, head2):
    start = None
    last = None
    if(head1.data < head2.data):
        start = head1
        head1 = head1.next
    else:
        start = head2
        head2 = head2.next
    last = start

    while head1 is not None and head2 is not None:
        if(head1.data < head2.data):
            last.next = head1
            last = head1

            head1 = head1.next
        else:
            last.next = head2
            last = head2

            head2 = head2.next

    if head1 is not None:
        last.next = head1
    elif head2 is not None:
        last.next = head2

    return start
