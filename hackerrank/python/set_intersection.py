m = int(input())
setM = set(map(int, input().split(" ")))
n = int(input())
setN = set(map(int, input().split(" ")))

print(len(list(setM.intersection(setN))))
