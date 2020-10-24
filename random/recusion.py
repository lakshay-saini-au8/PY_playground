'''
Factorial
'''
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)


# n = 5
# print(fact(n)) #120


'''
Sum of First N natural No.
'''


# def sumofN(n):
#     if n == 1:
#         return 1
#     return n + sumofN(n-1)


# n = 5
# print(sumofN(n)) #15

'''
print no from 1 to n and n to 1 in single program

'''


# def zero_to_one(n):
#     if n == 0:
#         print()
#         return
#     print(n, end=" ")
#     zero_to_one(n-1)
#     print(n, end=" ")
#     return


# n = 20
# zero_to_one(n)
# output
# 10 9 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 10


'''
Fibonaci series
'''


# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     fib_sum = fib(n-1) + fib(n-2)
#     return fib_sum


# n = 4
# print(fib(n)) #3

'''

Given a list whether it is sorted or not

'''


# def check_sort(arr, i, l):
#     if i == l or i == l-1:
#         return True

#     if arr[i] > arr[i+1]:
#         return False
#     if check_sort(arr, i+1, l):
#         return True
#     else:
#         return False


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(check_sort(arr, 0, len(arr))) #False

'''
Find the first Occurence

'''


# def firstIndex(arr, i, l, x):
#     if i == l:
#         return -1
#     if arr[i] == x:
#         return i
#     return firstIndex(arr, i+1, l, x)

# def firstIndex(arr, x):
#     l = len(arr)
#     if l == 0:
#         return -1
#     if arr[0] == x:
#         return 0
#     index = firstIndex(arr[1:], x)
#     if index == -1:
#         return -1
#     else:
#         return index+1


# arr = [2, 4, 5, 75, 6, 5, 5, 10]
# print(firstIndex(arr, 5)) #2
# print(firstIndex(arr, 0, len(arr), 5))#2


# def lastIndex(arr, l, x):
#     if l == 0:
#         return -1
#     if arr[l-1] == x:
#         return l-1
#     return lastIndex(arr, l-1, x)

# def lastIndex(arr, i, l, x):
#     if i == l:
#         return -1
#     if arr[l-1] == x:
#         return l-1
#     return lastIndex(arr, i+1, l-1, x)

# def lastIndex(arr, i, l, x):
#     if i == l:
#         return -1
#     last = lastIndex(arr, i+1, l, x)
#     if last != -1:
#         return last
#     else:
#         if arr[i] == x:
#             return i
#         else:
#             return -1


# arr = [2, 4, 5, 75, 6, 10, 5]
# # print(firstIndex(arr, 5)) #2
# print(lastIndex(arr, 0, len(arr), 5))  # 6

'''
replace orccurence of a with b in a string

'''


def replace(s, a, b):
    if len(s) == 0:
        return s
    small = replace(s[1:], a, b)
    if s[0] == a:
        return b + small
    else:
        return s[0]+small


print(replace('dacdxcd', 'c', 'x'))
