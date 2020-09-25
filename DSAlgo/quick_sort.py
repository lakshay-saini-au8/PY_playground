def partition(arr, start, end):
    last = arr[end]
    i = start
    j = start
    while j <= end-1:
        if arr[j] <= last:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[i], arr[end] = arr[end], arr[i]
    return i


def quick_sort(arr, start, end):
    if(start < end):
        part = partition(arr, start, end)
        quick_sort(arr, start, part-1)
        quick_sort(arr, part+1, end)


arr = [5, 4, 70, 8, 1]
quick_sort(arr, 0, len(arr)-1)
print(arr)
