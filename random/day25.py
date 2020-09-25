# print("Enter number of queens")
# N = int(input())

# board = [[0]*N for _ in range(N)]
# print(board)


# def n_queen(n):
#     if n == 0:
#         return True
#     for i in range(N):
#         for j in range(N):
#             if not(is_attack(i, j)) and board[i][j] != 1:
#                 board[i][j] = 1
#                 if n_queen(n-1) == True:
#                     return True
#                 board[i][j] = 0
#     return False


# def is_attack(i, j):
#     for k in range(N):
#         if board[i][k] == 1 or board[k][j] == 1:
#             return True
#         for k in range(N):
#             for l in range(N):
#                 if k+l == i+j or k-l == i-j:
#                     if board[k][l] == 1:
#                         return True
#     return False


# n_queen(N)
# print([print(i) for i in board])

size = 3
maze = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]
solution = [[0]*size for _ in range(size)]


def solvemaze(row, col):
    if row == size - 1 and col == size-1:
        solution[row][col] = 1
        return True
    if row >= 0 and col >= 0 and row < size and col < size and solution[row][col] == 0 and maze[row][col] == 1:
        solution[row][col] = 1
        if solvemaze(row+1, col):
            return True
        if solvemaze(row, col+1):
            return True
        if solvemaze(row-1, col):
            return True
        if solvemaze(row, col-1):
            return True
        solution[row][col] = 0
        return False
    return 0


if solvemaze(0, 0):
    for i in solution:
        print(i)
