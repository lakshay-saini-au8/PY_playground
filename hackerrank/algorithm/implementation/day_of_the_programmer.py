# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    day_count = 13
    if year >= 1919:

        if not(year % 100):
            if not(year % 400):
                day_count = 12
        else:
            if not(year % 4):
                day_count = 12
        return str(day_count)+".09."+str(year)
    elif year <= 1917:
        if year % 4 == 0:
            day_count = 12
        return str(day_count)+".09."+str(year)
    else:
        day_count = 26
        return str(day_count)+".09."+str(year)
