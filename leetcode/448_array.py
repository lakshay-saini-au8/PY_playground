#  que https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/solution/

# solution 1
def findDisappearedNumbers(arr):
    n = len(arr)
    arr = list(set(arr))
    for i in range(1, n+1):
        if(i in arr):
            arr.remove(i)
        else:
            arr.append(i)
    return arr


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

# solution 2


def findDisappearedNumbers(arr):
    n = len(arr)
    set_of_nums = set(range(1, n+1))
    arr = list(set(arr))
    for i in arr:
        if(i in set_of_nums):
            set_of_nums.remove(i)
    return list(set_of_nums)


print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
