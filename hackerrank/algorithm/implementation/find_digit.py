
# Complete the findDigits function below.
def findDigits(n):
    count = 0
    for i in str(n):
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1
    return count
