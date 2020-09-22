# https://www.hackerrank.com/challenges/equal-stacks/problem
def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    s1, s2, s3 = list(map(sum, (h1, h2, h3)))
    while s1 and s2 and s3:
        m = min(s1, s2, s3)
        while s1 > m:
            s1 = s1 - h1.pop()
        while s2 > m:
            s2 = s2 - h2.pop()
        while s3 > m:
            s3 = s3 - h3.pop()
        if s1 == s2 == s3:
            return s1
    return 0
    # Write your code here
