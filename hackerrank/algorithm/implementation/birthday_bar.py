# Complete the birthday function below.
def birthday(s, d, m):
    final_res = []

    for i in range(len(s)-m+1):
        sum_res = 0
        result = []
        for j in range(i, m+i):
            sum_res += s[j]
            result.append(s[j])

        if sum_res == d:
            if len(final_res) == 0:
                final_res.append(result)
            else:
                flag = False
                for i in final_res:
                    if i == result:
                        flag = True
                if flag != True:
                    final_res.append(result)

    return len(final_res)
