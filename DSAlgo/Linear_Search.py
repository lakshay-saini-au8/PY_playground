# Apporach:-
# Start from the leftmost element of arr and compare each element to x if you find that retrun index otherwise retrun -1.
# Time Complexity Worst Case:= O(n)
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = search(arr, x)
print(result)
