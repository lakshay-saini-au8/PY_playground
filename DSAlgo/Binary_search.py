# iterative solution
def binary_search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# recursive solution
def binary_search_rec(arr, l, r, x):
    if r >= 1:
        mid = (l+r) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_rec(arr, l, mid-1, x)
        else:
            return binary_search_rec(arr, mid+1, r, x)
    else:
        return -1


print(binary_search_rec([2, 3, 4, 10, 40], 0, 4, 10))
