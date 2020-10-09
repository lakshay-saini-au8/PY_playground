# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self, qn):
        while (len(self.s1) != 0):
            self.s2.append(self.s1.pop())
        if qn == 2:
            self.s2.pop()
        elif qn == 3:
            top_value = self.s2[-1]
            print(top_value)


stack_queue = Queue()

n = int(input())
for i in range(n):
    query = input()
    if len(query) > 1:
        query_no, data = list(map(int, query.split(" ")))
        stack_queue.enqueue(data)
    else:
        query_no = int(query)
        if query_no == 2:
            stack_queue.dequeue(query_no)
        elif query_no == 3:
            stack_queue.dequeue(query_no)
