# https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

def pickingNumbers(a):
    # Write your code here
    len_res = 0
    res_fin = []
    for i in a:
        res = []
        for j in a:
            if abs(i-j) == 1 or abs(i-j) == 0:
                if len(res) == 0:
                    res.append(j)
                else:
                    flag = False
                    for k in res:
                        if abs(j-k) > 1:
                            flag = True
                    if flag == False:
                        res.append(j)
        if len(res) > len_res:
            len_res = len(res)
            res_fin = res
    print(res_fin)
    return len_res
