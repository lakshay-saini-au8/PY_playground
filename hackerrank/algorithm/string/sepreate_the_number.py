# https://www.hackerrank.com/challenges/separate-the-numbers/problem?isFullScreen=false
# Complete the separateNumbers function below.

def separateNumbers(s):
    if len(s) == 1:
        print("NO")
        return
    else:
        # Half iter no need to go further
        for i in range(1, len(s)//2 + 1):
            new_str = s[:i]
            prev_str = int(new_str)
            while len(new_str) < len(s):
                str1 = prev_str + 1
                new_str = new_str + str(str1)
                prev_str = str1
            if new_str == s:
                print("YES", s[:i])
                return
        print("NO")
