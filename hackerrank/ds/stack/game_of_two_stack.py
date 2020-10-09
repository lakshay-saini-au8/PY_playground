def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    total_1 = 0
    arr1 = []
    arr2 = []
    i = 0
    while(i < len(a)):
        total_1 += a[i]
        if total_1 > x:
            break
        arr1.append(total_1)
        i += 1
    j = 0
    total_2 = 0
    while(j < len(b)):
        total_2 += b[j]
        if total_2 > x:
            break
        arr2.append(total_2)
        j += 1
    print(arr1, arr2)

    best_count = max(len(arr1), len(arr2))
    i = len(arr1)
    j = 0
    for k in range(i-1, -1, -1):
        current_sum = arr1[k]
        while j < len(arr2) and current_sum+arr2[j] <= x:
            j += 1
        next_count = k+1+j

        best_count = max(best_count, next_count)

    return best_count
