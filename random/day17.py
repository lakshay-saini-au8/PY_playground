# 10 matrix example
from numpy import *

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = matrix(list1)
secarr = matrix(list2)
# 1
print(arr)
arr2 = arr.flatten()
print(arr2)

# 2
arr3 = arr2.reshape(3, 3)
print(arr3)

# 3
arr4 = arr + secarr
print(arr4)

# 4
arr5 = arr * secarr
print(arr5)

# 5
print(arr5.diagonal())

# 6
print(arr5.trace())

# 7
print(arr5.min())

# 8
print(arr5.max())

# 9
print(arr5.mean())

# 10
print(arr5.transpose())
