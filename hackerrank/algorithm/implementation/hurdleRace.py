# https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Complete the hurdleRace function below.
def hurdleRace(k, height):
    max_height = max(height)
    jump = k-max_height
    if jump < 0:
        return abs(jump)
    else:
        return 0
