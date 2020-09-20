# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem?isFullScreen=true
# sol1
def findMergeNode(head1, head2):
    temp1 = head1
    while temp1 is not None:
        temp2 = head2
        while temp2 is not None:
            if temp1 == temp2:
                print("hello")
                return temp1.data
            else:
                print("bye")
                temp2 = temp2.next
        temp1 = temp1.next
