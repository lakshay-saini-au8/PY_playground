n = int(input())
pos = input().split().index("MARKS")
scores = []
for _ in range(n):
    field = input().split()[pos]
    scores.append(int(field))
print("{:.2f}".format(sum(scores)/n))
