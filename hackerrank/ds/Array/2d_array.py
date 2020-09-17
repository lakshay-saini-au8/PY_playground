# https://www.hackerrank.com/challenges/2d-array/problem
# Complete the hourglassSum function below.
def hourglassSum(arr):
    result = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            total = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    total = total + arr[k][l]

            total = total - arr[i+1][j] - arr[i+1][j+2]
            result.append(total)
    return max(result)
