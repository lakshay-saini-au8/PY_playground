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


def serach(nums, target):
    start = 0
    end = len(nums)-1
    first = nums[0]
    while start <= end:
        mid = (start+end)//2
        value = nums[mid]
        if value == target:
            return mid
        if value >= first:
            start = mid+1
        elif value <= first:
            end = mid - 1

    bigger = nums[0:start]
    smaller = nums[start:]
    if len(smaller) == 0:
        return binary_search(bigger, target)
    else:
        tar1 = binary_search(bigger, target)
        if tar1 != -1:
            return tar1
        tar2 = binary_search(smaller, target)
        return tar2+len(bigger)
    return -1


print(serach([4, 5, 1, 2, 3], 5))
