# find the reverse of a string using recursion

def rev_rec(s):
    strs = ""
    if len(s) == 0:
        return s
    s = rev_rec(s[1:])+s[0]
    return s


# print(rev_rec("hello"))

# find the sum of first N natural number using recursion

def sum_rec(n):
    if n == 1:
        return 1
    n = n + sum_rec(n-1)
    return n


print(sum_rec(5))

# check weather a string is palindrome or not using rec:-


def pal_rec(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return pal_rec(s[1:-1])


print(pal_rec("m"))
