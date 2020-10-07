# https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true

# Complete the angryProfessor function below.
def angryProfessor(n, k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    if count >= k:
        return "NO"
    else:
        return "YES"
