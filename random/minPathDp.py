import sys


def minCost(i, j, n, m):
    if i == n-1 and j == m-1:
        return cost[i][j]
    if i >= n or j >= m:
        return sys.maxsize
    return cost[i][j] + min(minCost(i, j+1, n, m), minCost(i+1, j, n, m), minCost(i+1, j+1, n, m))


cost = [[1, 5, 11], [8, 13, 12], [2, 3, 7], [15, 16, 18]]
ans = minCost(0, 0, 4, 3)
print(ans)
