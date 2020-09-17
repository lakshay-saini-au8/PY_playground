# https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=false

def dynamicArray(n, queries):
    # Write your code herere
    result = []
    lastAnswer = 0
    final = []
    for _ in range(n):
        result.append([])
    for query_no, x, y in queries:
        if query_no == 1:
            index = ((x ^ lastAnswer) % n)
            result[index].append(y)
        if query_no == 2:
            index = ((x ^ lastAnswer) % n)
            size = len(result[index])
            seq_index = y % size
            lastAnswer = result[index][seq_index]
            final.append(lastAnswer)
    return final
