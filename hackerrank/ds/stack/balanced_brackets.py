# https://www.hackerrank.com/challenges/balanced-brackets/problem
# Complete the isBalanced function below.
def isBalanced(s):
    s1 = []
    for i in range(len(s)):
        if len(s1) == 0:
            s1.append(s[i])
        else:
            check = None
            if s1[-1] == "(":
                check = ")"
            elif s1[-1] == "{":
                check = "}"
            elif s1[-1] == "[":
                check = "]"
            if check == str(s[i]):
                s1.pop()

            else:
                s1.append(s[i])
    print(s1)

    if len(s1) == 0:
        return "YES"
    else:
        return "NO"
