# que https://leetcode.com/problems/sort-array-by-parity/submissions/

# solution1
# def sortArrayByParity(A):
#     newArr = []
#     for i in A:
#         if(i % 2 == 0):
#             newArr.insert(0, i)
#         else:
#             newArr.append(i)

#     return newArr

# solution 2
def sortArrayByParity(A):
    i = 0
    for j in range(len(A)):
        if(A[j] % 2 == 0):
            A[i], A[j] = A[j], A[i]
            i = i+1
    return A


print(sortArrayByParity([3, 1, 2, 4]))
