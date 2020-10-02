# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_num = sys.maxsize
    max_num = 0
    count = 0
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(n):
            if i != j:
                total += arr[j]
        if min_num > total:
            min_num = total
        if max_num < total:
            max_num = total

    print(f"{min_num} {max_num}")
