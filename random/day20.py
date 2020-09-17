def binary_search(arr, x):
    startbs = 0
    endbs = len(arr) - 1
    while startbs <= endbs:
        midbs = (startbs+endbs) // 2
        if arr[midbs] == x:
            return midbs
        elif arr[midbs] < x:
            startbs = midbs + 1
        else:
            endbs = midbs - 1
    return -1


def Search(arr, k, n):
    pivot = 0
    start = 0
    end = n-1
    while start <= end:
        mid = (start+end)//2
        # print(start,end)
        # print(mid)
        if arr[mid] > k:
            end = mid-1
            if arr[mid+1] > arr[mid]:
                pivot = mid
                break
        elif arr[mid] < k:
            start = mid+1
            if arr[mid-1] > arr[mid]:
                pivot = mid
                break
    arr1 = arr[:pivot]
    arr2 = arr[pivot:]

    if arr1[len(arr1)-1] >= k:
        return binary_search(arr1, k)
    else:
        return binary_search(arr2, k)


print(Search([5, 6, 7, 8, 9, 10, 1, 2, 3], 10, 9))
print(Search([3, 1, 2], 3, 3))
