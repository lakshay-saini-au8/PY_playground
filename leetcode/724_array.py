
def pivotIndex(nums):
    l = len(nums)
    index = -1
    if (l == 1):
        index = 0
    elif (l == 0):
        index = -1
    else:
        for i in range(l):

            print(nums[:(i)-l], nums[i+1:])
            if (sum(nums[:(i)-l]) == sum(nums[i+1:])):
                index = i
                return index
    return index


print(pivotIndex([-1, -1, 0, 0, -1, -1]))
