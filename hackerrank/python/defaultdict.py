# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
d = defaultdict(list)
n, m = list(map(int, input().split(" ")))

for _ in range(n):
    d["A"].append(input())
for _ in range(m):
    d["B"].append(input())

for value in d['B']:
    flag = 0
    result = []
    for index, item in enumerate(d['A']):
        if value == item:
            result.append(index+1)
            flag = 1

    if flag == 0:
        print(-1)
    else:
        print(" ".join(list(map(str, result))))
