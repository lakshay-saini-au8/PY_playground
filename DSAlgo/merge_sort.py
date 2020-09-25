def merge(L, R, arr):
    i = 0
    j = 0
    k = 0
    l = len(L)
    r = len(R)
    while i < l and j < r:
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i+1
        else:
            arr[k] = R[j]
            j = j+1
        k = k+1
    while(i < l):
        arr[k] = L[i]
        i += 1
        k += 1
    while(j < r):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr):
    if(len(arr) > 1):
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, arr)


arr = [5, 45, 10, 4, 20, -1, -2]
merge_sort(arr)
print(arr)
