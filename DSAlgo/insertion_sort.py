def instertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        loc = i-1
        while loc >= 0 and arr[loc] > key:
            arr[loc+1] = arr[loc]
            loc = loc - 1
        arr[loc+1] = key


arr = [6, 8, 1, 4, 10, 9]
instertion_sort(arr)
print(arr)
