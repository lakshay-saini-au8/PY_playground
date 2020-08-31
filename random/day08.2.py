# que
'''
1 
3 5 
7 9 11 
13 15 17 19 
'''


def patter2(n):
    k = 1
    for i in range(n):
        for j in range(i+1):
            print(k, end=" ")
            k = k+2
        print()


patter2(4)
