'''

Question:1
Write a program to implement stack data structure in python with basic and auxiliary
operations like (push,pop,isEmpty,isFull,top,size,display).
'''


class Stack:
    def __init__(self):
        self.stack = []

    # check weather a stack is empty or not
    def isEmpty(self):
        return self.stack == []

    # add data to stack
    def push(self, item):
        self.stack.append(item)

    # pop data from stack
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # get the top stack item
    def peek(self):
        return self.stack[-1]

    # get the size of stack
    def size(self):
        return len(self.stack)

    # print the size
    def print_stack(self):
        for i in self.stack:
            print(i, end=" ")


# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(440)
# s.push(5)
# s.print_stack()
# print()
# print(s.peek())
# print(s.size())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# s.print_stack()
# print()
# print(s.peek())
# print(s.size())

'''
Question:3
Write a program to reverse a number using stack.
Input : 365
Output : 563
Input : 6899
Output : 9986
'''
