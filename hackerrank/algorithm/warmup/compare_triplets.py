# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for i in range(3):

        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1
    return [alice, bob]
