# https://www.hackerrank.com/challenges/crush/problem

# Complete the arrayManipulation function below.
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    result = [0]*n

    for a, b, k in queries:
        for i in range(a-1, b):
            result[i] = result[i]+k

    return max(result)
