# https: // www.hackerrank.com/challenges/sparse-arrays/problem
# Complete the matchingStrings function below.


def matchingStrings(strings, queries):
    result = []
    for value in queries:
        count = 0
        for item in strings:
            if value == item:
                count = count + 1
        result.append(count)
    return result
