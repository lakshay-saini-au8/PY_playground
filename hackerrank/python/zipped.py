# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = list(map(int, input().split()))
x = []
for _ in range(m):
    x.append(list(map(float, input().split())))

for i in list(zip(*x)):
    print(sum(i)/m)
