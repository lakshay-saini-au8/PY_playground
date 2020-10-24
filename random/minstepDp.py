import sys


def minstepto1(n, dp):
    if n == 1:
        return 0
    div2 = sys.maxsize
    if n % 2 == 0:
        num2 = n//2
        if dp[num2] != -1:
            div2 = dp[num2]

        else:
            div2 = minstepto1(n//2, dp)
            dp[num2] = div2
    div3 = sys.maxsize
    if n % 3 == 0:
        num3 = n//3
        if dp[num3] != -1:
            div3 = dp[num3]
        else:
            div3 = minstepto1(n//3, dp)
            dp[num3] = div3
    if dp[n-1] != -1:
        div1 = dp[n-1]
    else:
        div1 = minstepto1(n-1, dp)
        dp[n-1] = div1
    return min(div1, div2, div3) + 1


n = 100
dp = [-1 for _ in range(n+1)]

print(minstepto1(n, dp))
