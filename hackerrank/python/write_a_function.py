# question https://www.hackerrank.com/challenges/write-a-function/problem
#solution

def is_leap(year):
    leap = False
    
    # Write your logic here
    if not(year%100):
        if not(year%400):
            leap = True
    else:
        if not(year%4):
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))