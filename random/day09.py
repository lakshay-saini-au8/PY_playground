'''
1. Write a Python function that takes a number as a parameter and checks if the
number is prime or not.
'''
import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            print(f"{n} is a not prime number")
            return
        else:
            print(f"{n} is a prime number")
            return


is_prime(11)
is_prime(12)


'''
2. Write a Python function that accepts a string and calculates the number of uppercase
letters and lowercase letters.
'''


def calc_ul_ll(str):
    ul = 0
    ll = 0
    for ch in str:
        if (ch.islower()):
            ll = ll + 1
        elif(ch.isupper()):
            ul = ul+1
    return ul, ll


ulc, llc = calc_ul_ll("Hello don HERE YOU")
print(f" Upper case character count is {ulc}")
print(f" Lower case character count is {llc}")
