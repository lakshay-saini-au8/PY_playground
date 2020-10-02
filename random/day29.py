'''
Write a program to find the most frequent element in an array(Use Hashing
Technique).
Input : arr[] = {1, 3, 2, 1, 4, 1}
Output : 1
1 appears three times in array which
is maximum frequency.
Input : arr[] = {10, 20, 10, 20, 30, 20, 20}
Output : 20
'''


def most_freq(arr):
    hash_ = dict()
    max_count = 0
    max_index = 0
    n = len(arr)
    for i in range(n):
        if arr[i] in hash_.keys():
            hash_[arr[i]] += 1
            value = hash_[arr[i]]
            if max_count < value:
                max_count = value
                max_index = arr[i]
        else:
            hash_[arr[i]] = 1
    print(max_index)


most_freq([1, 3, 2, 1, 4, 1])
most_freq([10, 20, 10, 20, 30, 20, 20])


'''
Question:2
Write a program to sort elements by frequency(Use Hashing Technique).
Print the elements of an array in the decreasing frequency if 2 numbers have the same
frequency then print the one which came first.
Input: arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}
'''


def sort_by_freq(arr):
    result = []
    hash_ = dict()
    n = len(arr)
    for i in range(n):
        if arr[i] in hash_.keys():
            hash_[arr[i]] += 1
        else:
            hash_[arr[i]] = 1
    list_of_item = list(hash_.items())
    n_list = len(list_of_item)
    for i in range(n_list):
        for j in range(n_list-i-1):
            if list_of_item[j][1] < list_of_item[j+1][1]:
                list_of_item[j], list_of_item[j +
                                              1] = list_of_item[j+1], list_of_item[j]

    for key, value in list_of_item:
        for _ in range(value):
            result.append(key)

    print(result)


sort_by_freq([2, 5, 2, 8, 5, 6, 8, 8])
sort_by_freq([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8])


'''
Question:3
Write a program to find any one of the multiple repeating elements in the read
only array(Use Hashing Technique).
Given a read only array of size ( n+1 ), find one of the multiple repeating elements in the
array where the array contains integers only between 1 and n.
Input : n = 5
arr[] = {1, 1, 2, 3, 5, 4}
Output : One of the numbers repeated in the array is: 1
Input : n = 10
arr[] = {10, 1, 2, 3, 5, 4, 9, 8, 5, 6, 4}
Output : One of the numbers repeated in the array is: 4 OR 5
'''


def one_multi(arr):
    hash_ = dict()
    n = len(arr)
    for i in range(n):
        if arr[i] in hash_.keys():
            hash_[arr[i]] += 1
            value = hash_[arr[i]]
            if value >= 2:
                return arr[i]
        else:
            hash_[arr[i]] = 1


print(one_multi([1, 1, 2, 3, 5, 4]))
print(one_multi([10, 1, 2, 3, 5, 4, 9, 8, 5, 6, 4]))
