# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
def removeDuplicates(head):
    temp = head
    while temp.next is not None:
        if temp.data == temp.next.data:
            del_node = temp.next
            temp.next = del_node.next
            del del_node
        else:
            temp = temp.next
    return head
