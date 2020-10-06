def countingValleys(steps, path):
    # Write your code here
    count_valley = 0
    sea_level = False
    level = 0
    for i in range(steps):
        if path[i] == "U":
            level += 1
        elif path[i] == "D":
            level -= 1
        if not(sea_level) and level < 0:
            count_valley += 1
            sea_level = True
        if level >= 0:
            sea_level = False
    return count_valley
