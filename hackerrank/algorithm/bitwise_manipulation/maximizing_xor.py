# https://www.hackerrank.com/challenges/maximizing-xor/problem
def maximizingXor(l, r):
    max_num = -1
    for i in range(l, r+1):
        res = []
        for j in range(l, r+1):
            res.append(i ^ j)
        res_max = max(res)
        if res_max > max_num:
            max_num = res_max
    return max_num


print(3 ^ 1)
