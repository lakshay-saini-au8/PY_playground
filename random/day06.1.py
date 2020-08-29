'''
Write a program to find the greatest common divisor(gcd) of two numbers given from the user
input.
Task 1: Write program using while Loop
Task 2: Write program using for loop

'''


def gcd(a, b):
    gcd = 1
    n = 1
    if a > b:
        n = a
    else:
        n = b
    # using for loop if you want to you use this just uncomment this
    # for i in range(2, n+1):
    #     if(a % i == 0 and b % i == 0):
    #         gcd = i

    # using while loop
    i = 2
    while (i <= n):
        if(a % i == 0 and b % i == 0):
            gcd = i
        i = i+1

    print(gcd)


gcd(48, 56)
