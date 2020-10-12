# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for i in range(i, j+1):
        reverse = int(str(i)[::-1])
        if(abs(i-reverse) % k) == 0:
            count += 1
    return count
