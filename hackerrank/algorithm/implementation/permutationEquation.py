# https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true
# Complete the permutationEquation function below.
def permutationEquation(p):
    x = 1
    hash_ = dict()
    res = []
    for key, value in enumerate(p):
        hash_[value] = key+1
    print(hash_)
    while x <= len(p):
        value_at_x = hash_[x]
        value_for_y = hash_[value_at_x]
        res.append(value_for_y)
        x += 1
    return res
