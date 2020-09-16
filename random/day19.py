def first_occurence(arr, x):
    start = 0
    end = len(arr) - 1
    first = -1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == x:
            first = mid
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return first


def last_occurence(arr, x):
    start = 0
    end = len(arr) - 1
    last = -1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == x:
            last = mid
            start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return last


print(first_occurence([2, 5, 9, 11, 11, 11, 11, 15], 11))
print(last_occurence([2, 5, 9, 11, 11, 11, 11, 15], 11))
print(first_occurence([101, 110, 114, 114, 114, 114, 1001], 114))
print(last_occurence([101, 110, 114, 114, 114, 114, 1001], 114))

first_index = first_occurence([101, 110, 114, 114, 114, 114, 1001], 114)
last_index = last_occurence([101, 110, 114, 114, 114, 114, 1001], 114)
count = (last_index - first_index) + 1
print(f"count of 114 is : {count}")


def Array2D(m, n):
    result = []
    for i in range(m):
        matrix = []
        for j in range(n):
            matrix.append(i*j)
        result.append(matrix)
    print(result)


Array2D(4, 4)
