# recursive type
# def fibb(n, dp):
#     if n == 0 or n == 1:
#         return n
#     if dp[n-1] == -1:
#         res1 = fibb(n-1, dp)
#         dp[n-1] = res1
#     else:
#         res1 = dp[n-1]
#     if dp[n-2] == -1:
#         res2 = fibb(n-2, dp)
#         dp[n-2] = res2
#     else:
#         res2 = dp[n-2]

#     return res1 + res2


# iterative sol


n = 10


def fibbI(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    i = 2
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]


print(fibbI(n))
