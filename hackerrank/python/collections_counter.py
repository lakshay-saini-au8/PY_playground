# https://www.hackerrank.com/challenges/collections-counter/problem
n = int(input())
size_list = list(map(int, input().split(" ")))
no_of_customers = int(input())
total_sum = 0
for _ in range(no_of_customers):
    size, price = list(map(int, input().split(" ")))
    if size in size_list:
        size_list.remove(size)
        total_sum = total_sum+price

print(total_sum)
