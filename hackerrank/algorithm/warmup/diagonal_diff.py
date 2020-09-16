
# https://www.hackerrank.com/challenges/diagonal-difference/problem
def diagonalDifference(arr):
    # Write your code here
    # frist diagonal
    n = len(arr)
    m = len(arr[0])
    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 = diag1 + arr[i][i]
    for i in range(n):
        m = m-1
        diag2 = diag2 + arr[i][m]

    return abs(diag1-diag2)
