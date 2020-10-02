# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_num = scores[0]
    max_count = 0
    min_num = scores[0]
    min_count = 0
    for i in range(1, len(scores)):
        if min_num > scores[i]:
            min_num = scores[i]
            min_count += 1
        elif max_num < scores[i]:
            max_num = scores[i]
            max_count += 1
    return [max_count, min_count]
