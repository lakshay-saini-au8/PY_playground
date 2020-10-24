import math
import sys


def minSquares(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        currAns = 1 + minSquares(n-(i**2))
        ans = min(currAns, ans)
    return ans


n = 28
ans = minSquares(n)
print(ans)
