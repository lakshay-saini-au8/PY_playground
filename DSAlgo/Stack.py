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


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(440)
s.push(5)
s.print_stack()
print()
print(s.peek())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
s.print_stack()
print()
print(s.peek())
print(s.size())
