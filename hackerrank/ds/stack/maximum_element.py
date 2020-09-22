# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
m = []
s = []

for _ in range(n):
    query = input()
    if len(query) > 1:
        query_no, data = list(map(int, query.split(" ")))
    else:
        query_no = int(query)

    if query_no == 1:
        if len(s) == 0:
            m.append(data)
            s.append(data)
            continue

        if m[-1] < data:
            m.append(data)
        else:
            m.append(m[-1])
        s.append(data)

    elif query_no == 2:
        if len(s) != 0:
            s.pop()
            m.pop()

    else:
        print(m[-1])
