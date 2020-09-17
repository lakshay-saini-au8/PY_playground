def findExtra(a, b):
    start = 0
    end = len(a)-1
    index=len(a)
    if a[len(a)-1] != b[len(b)-1]:
        return len(a)-1
    while start <= end:
        mid = (start+end)//2
        if a[mid] == b[mid]:
            start = mid+1
        elif a[mid] < b[mid]:
            end = mid - 1
            index = mid
    return index

print(findExtra([2, 4, 6, 8, 9, 10, 12], [2, 4, 6, 8, 10, 12]))
print(findExtra([3, 5, 7, 9, 11, 13], [3, 5, 7, 11, 13]))

print(findExtra([1,2,3,4], [1,3,4]))