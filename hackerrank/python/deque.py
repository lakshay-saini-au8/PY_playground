from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    query = input()

    if query == "pop":
        d.pop()
        continue
    elif query == "popleft":
        d.popleft()
        continue
    query, value = query.split()
    if query == "append":
        d.append(value)
        continue
    elif query == "appendleft":
        d.appendleft(value)
        continue
for i in d:
    print(i, end=" ")
