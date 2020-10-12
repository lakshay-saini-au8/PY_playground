# Complete the minimumDistances function below.
def minimumDistances(a):
    n = len(a)
    min_dis = []
    for i in range(n):
        arr = a[i+1:]
        if a[i] in arr:
            dis = abs(i-(arr.index(a[i])+i+1))
            min_dis.append(dis)
    if len(min_dis) == 0:
        return -1
    else:
        return min(min_dis)
