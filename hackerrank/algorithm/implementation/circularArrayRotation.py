# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    res = []
    for _ in range(k):
        poped = a.pop()
        a.insert(0, poped)
    for i in queries:
        res.append(a[i])
    return res
