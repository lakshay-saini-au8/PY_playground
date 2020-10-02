def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    n = len(arr)
    for i in arr:
        if i >0:
            pos += 1
        elif i <0:
            neg += 1
        else:
            zero += 1
    
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))