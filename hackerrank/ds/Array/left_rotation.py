# https://www.hackerrank.com/challenges/array-left-rotation/problem

def rotateLeft(d, arr):
    # Write your code here
    if len(arr) == d:
        return arr
    else:
        arr1 = arr[0:d]
        arr2 = arr[d:]
        arr2.extend(arr1)
        return arr2
