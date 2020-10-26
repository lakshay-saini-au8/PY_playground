# def merge(left, right, a):

#     i = 0
#     j = 0
#     k = 0
#     while i < len(left) and j < len(right):
#         if left[i] > right[j]:
#             a[k] = right[j]
#             k += 1
#             j += 1
#         else:
#             a[k] = left[i]
#             k += 1
#             i += 1
#     while i < len(left):
#         a[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         a[k] = right[j]
#         k += 1
#         j += 1


# def merge_sort(a):
#     if len(a) == 0 or len(a) == 1:
#         return
#     mid = len(a) // 2
#     a1 = a[0:mid]
#     a2 = a[mid:]
#     merge_sort(a1)

#     merge_sort(a2)
#     merge(a1, a2, a)


# a = [10, 5, 3, 1, 7, 9, 4]
# merge_sort(a)
# print(a)


'''
quick sort
'''


def partition(arr, s, e):
    pivot = e
    i = s
    j = s
    while j < e:
        if arr[j] < arr[pivot]:

            arr[i], arr[j] = arr[j], arr[i]
            i += 1

        j += 1

    arr[i], arr[pivot] = arr[pivot], arr[i]
    return i


def quick_sort(arr, s, e):
    if s >= e:
        return
    pivot = partition(arr, s, e)
    quick_sort(arr, s, pivot-1)
    quick_sort(arr, pivot+1, e)


arr = [10, 9, 8, 7, 1, 3, 5, 4, 2]
print(quick_sort(arr, 0, len(arr)-1))
print(arr)
