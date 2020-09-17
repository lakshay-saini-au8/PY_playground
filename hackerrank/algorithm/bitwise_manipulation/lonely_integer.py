# https://www.hackerrank.com/challenges/lonely-integer/problem
def lonelyinteger(a):
    result = 0
    for item in a:
        result = result ^ item
    return result
