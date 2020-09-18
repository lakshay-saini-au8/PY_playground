# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem?isFullScreen=true

def compare_lists(llist1, llist2):
    temp1 = llist1
    temp2 = llist2
    if temp1 is None and temp2 is None:
        return 1
    while temp1 is not None or temp2 is not None:

        if (temp1 is None and temp2 is not None) or (temp2 is None and temp1 is not None):
            return 0
        else:
            if temp1.data is not temp2.data:
                return 0
        temp1 = temp1.next
        temp2 = temp2.next
    return 1
