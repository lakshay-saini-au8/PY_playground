# Complete the camelcase function below.
def camelcase(s):
    count = 1
    for i in s:
        if i.isupper():
            count += 1
    return count


sr = "10"
print(sr*10+"hello")
