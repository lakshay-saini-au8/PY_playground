# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    TA = 0
    TO = 0
    for i in range(len(apples)):
        apples[i] += a
        if apples[i] >= s and apples[i] <= t:
            TA += 1
    print(TA)
    for j in range(len(oranges)):
        oranges[j] += b
        if oranges[j] >= s and oranges[j] <= t:
            TO += 1
    print(TO)
