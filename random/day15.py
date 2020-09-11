def subArraySum(arr, n, sum):
    # Your code here
    flag = False
    i = 0
    j = 0
    subsum = 0
    while(j < n):
        if subsum < sum:
            subsum = subsum + arr[j]
            j = j + 1
        else:
            if subsum == sum:
                flag = True
                print(subsum)
                break
            else:
                i = i+1
                j = i
                subsum = 0

    if flag:
        print(i+1, j)
    else:
        print("-1")


subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15)
