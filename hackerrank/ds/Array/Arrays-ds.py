# https://www.hackerrank.com/challenges/arrays-ds/problem
# Complete the reverseArray function below.
def reverseArray(a):
    result = []
    for i in range(len(a)):
        result.append(a.pop())

    return result
