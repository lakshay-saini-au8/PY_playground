# Task1
'''
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''
# def reverse_pattern(n):
#     for i in range(n, 0, -1):
#         for j in range(0, abs(n-i)):
#             print(end="  ")
#         for k in range(0, i):
#             print("*", end=" ")
#         print()

# Task 2
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *
'''


def reverse_pattern(n):
    for i in range(0, n):
        for j in range(n-(i+1), 0, -1):
            print(end="  ")
        for k in range(0, i):
            print("*", end=" ")
        print()


# taks 3
'''
* 
* * 
* * * 
* * * * 
* * * 
* * 
* 
'''


def reverse_pattern(n):
    for i in range(0, n+1):
        for k in range(0, i):
            print("*", end=" ")
        print()

    for j in range(n-1, 0, -1):
        for _ in range(0, j):
            print("*", end=" ")
        print()


reverse_pattern(6)
