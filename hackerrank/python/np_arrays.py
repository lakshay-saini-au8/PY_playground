#https://www.hackerrank.com/challenges/np-arrays/problem

#solution

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr.reverse()
    b = numpy.array(arr,float)
    return b

arr = input().strip().split(' ')
result = arrays(arr)
print(result)