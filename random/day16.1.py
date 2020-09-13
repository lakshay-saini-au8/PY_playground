# # q1. Write a program which moves all the zero’s to the end of the array.
def zero_to_end(arr):
    i = 1
    j = 1
    for value in arr:
        if value != 0:
            if i == j:
                i = i+1
                j = j+1
            else:
                temp = arr[i-1]
                arr[i-1] = arr[j-1]
                arr[j-1] = temp
                i = i+1
                j = j+1
        else:
            j = j+1
    print(arr)


zero_to_end([1, 2, 0, 4, 3, 0, 5, 0])

# q2.Rearrange positive and negative numbers where negative numbers come before positive numbers.


def rearrange(nums):
    arr1 = []
    arr2 = []
    for value in nums:
        if value >= 0:
            arr1.append(value)
        else:
            arr2.append(value)

    arr2.extend(arr1)

    print(arr2)


rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6])

# q3.Replace every array element by multiplication of previous and next


def mulprevnext(nums):
    result = []
    for index, value in enumerate(nums):
        if index == 0:
            result.append(nums[index]*nums[index+1])
        elif index == len(nums)-1:
            result.append(nums[index-1]*nums[index])
        else:
            result.append(nums[index-1]*nums[index+1])

    print(result)


mulprevnext([2, 3, 4, 5, 6])

# q4. Write a program to remove all the duplicates from the array and print it .


def removedup(nums):
    result = []
    for value in nums:
        if value in result:
            continue
        else:
            result.append(value)
    print(result)


removedup([5, 2, 1, 7, 1, 5, 2, 6, 8, 1, 2, 9])
