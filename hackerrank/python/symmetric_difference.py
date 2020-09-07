# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
setM = set(list(map(int, input().split(" "))))
n = int(input())
setN = set(list(map(int, input().split(" "))))

intersec = setM.intersection(setN)
uni = setM.union(setN)


result = sorted(list(uni.difference(intersec)))
[print(i) for i in result]
