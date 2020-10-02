# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):

    if x1 < x2 and v1 > v2:
        jump = 1
        while True:
            if x1+v1*jump == x2+v2*jump:
                return "YES"
            elif x1+v1*jump > x2+v2*jump:
                return "NO"
            jump += 1
    elif x1 > x2 and v1 < v2:
        jump = 1
        while True:
            if x1+v1*jump == x2+v2*jump:
                return "YES"
            elif x1+v1*jump < x2+v2*jump:
                return "NO"
            jump += 1

    else:
        return "NO"
