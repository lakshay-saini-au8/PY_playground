# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?isFullScreen=true
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA_dis = abs(z-x)
    catB_dis = abs(z-y)
    if catA_dis > catB_dis:
        return "Cat B"
    elif catA_dis < catB_dis:
        return "Cat A"
    else:
        return "Mouse C"
