# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    hash_ = dict()
    pairs = 0
    for i in ar:
        if i in hash_.keys():
            hash_[i] += 1
        else:
            hash_[i] = 1
    for item in hash_.values():
        if item % 2 == 0:
            count = item // 2
            pairs += count
        else:
            count = (item-1)//2
            pairs += count
    return pairs
