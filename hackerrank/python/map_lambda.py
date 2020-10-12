# cube = lambda x: x*x*x
def cube(x):
    return x*x*x


def fibonacci(n):
    # return a list of fibonacci numbers
    res = []
    if n > 2:
        res = [0, 1]
        for i in range(2, n):
            res.append(res[i-2]+res[i-1])
    elif n == 1:
        res = [0]
    elif n == 2:
        res = [0, 1]
    return res
