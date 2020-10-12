# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
n = int(input())
arr = input().split()
k = int(input())
count = 0
all_combination = list(combinations(arr, k))
for i in all_combination:
    if 'a' in i:
        count += 1
print(count/len(all_combination))
