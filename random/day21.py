# Question 1:Write a fibonacci program with and without recursion and also derive time complexities of both the programs.
def fib_without_rec(n):
    a = 0
    b = 1
    if n > 2:
        print(a, end=" ")
        print(b, end=" ")
        for i in range(3, n+1):
            print(a+b, end=" ")
            temp = b
            b = a+b
            a = temp
        print()


# time complexity
'''
O(n)

'''


def fib_with_rec(n):
    if n <= 1:
        return n
    else:
        return fib_with_rec(n-1) + fib_with_rec(n-2)

# time complexity
'''
O(n^2)

'''
for i in range(4):
    print(fib_with_rec(i), end=" ")
print()
fib_without_rec(4)


# Question 2: Write a factorial program with and without recursion and also derive time complexities of both the programs.

def fact_without_rec(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)


# time complexity
'''
O(n)

'''


def fact_with_rec(n):

    if n == 1:
        return 1
    return n * fact_with_rec(n-1)


# fact_without_rec(5)
# print(fact_with_rec(4))
# time complexity
'''
T(n) = T(n-1)+1
O(n)

'''
