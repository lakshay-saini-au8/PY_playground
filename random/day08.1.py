# que
'''
  a 
  b c 
 d e f 
g h i j 

'''


def abc_patter(n):
    k = n-1
    alpha = ord("a")
    for i in range(n):
        for _ in range(k):
            print(" ", end="")
        for j in range(i+1):
            print(chr(alpha), end=" ")
            alpha = alpha + 1

        k = k-1

        print()


abc_patter(4)
