'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

'''
# solution


def isMatrix(matrix):
    m, n = len(matrix), len(matrix[0])

    for i in range(m-1, 0, -1):
        for j in range(0, n-1):
            if matrix[i-1][j] != matrix[i][j+1]:
                return False

    return True


print(isMatrix([
    [1, 2, 4, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]))
