def countOccurence(arr, n, k):
    times = n//k
    count = 0
    obj = {}
    for i in arr:
        if i in list(obj.keys()):
            obj[i] = obj[i] + 1
            if (obj[i] > times):
                count = count + 1
        else:
            obj[i] = 1
    print(obj)
    print(count)


countOccurence([3, 1, 2, 2, 1, 2, 3, 3], 8, 4)
countOccurence([2, 3, 3, 2], 4, 3)
