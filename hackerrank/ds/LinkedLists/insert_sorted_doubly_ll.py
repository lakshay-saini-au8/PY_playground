# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
def sortedInsert(head, data):
    temp = head
    pos = head
    while temp.next is not None:
        if temp.data >= data:
            break
        else:
            temp = temp.next
    new_node = DoublyLinkedListNode(data)
    if temp.next is None:
        if temp.data <= data:
            new_node.prev = temp
            temp.next = new_node
            new_node.next = None
        else:
            new_node.next = temp
            new_node.prev = temp.prev
            new_pos = temp.prev
            new_pos.next = new_node
            temp.prev = new_node

    elif temp.prev is None:
        new_node.next = temp
        temp.prev = new_node
        head = new_node
    else:
        new_pos = temp.prev
        new_node.next = temp
        new_node.prev = new_pos
        temp.prev = new_node
        new_pos.next = new_node
    return head
