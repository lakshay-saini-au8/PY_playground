

# Write a program to find a triplet that sums to a given value with improved time complexity.
'''
Input: array = {12, 3, 4, 1, 6, 9}, sum = 24;
Output: 12, 3, 9
Explanation: There is a triplet (12, 3 and 9) present
in the array whose sum is 24.
'''

# brute force apporach


def triplet(arr, sums):
    n = len(arr)
    if n < 3:
        return "Array length is sort"
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k] == sums:
                    print(arr[i], arr[j], arr[k])


# triplet([12,3,4,1,6,9],24)
# triplet([1,2,3,4,5],9)


# Write a program to find a triplet such that the sum of two equals to the third element with improved time complexity

def triplet_sum(arr):
    n = len(arr)
    if n < 3:
        return "Array length is sort"
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i]+arr[j] == arr[k] or arr[j]+arr[k] == arr[i] or arr[k]+arr[i] == arr[j]:
                    print(arr[i], arr[j], arr[k])


triplet_sum([5, 32, 1, 7, 10, 50, 19, 21, 2])
# triplet_sum([5,32,1,7,10,50,19,21,0])
