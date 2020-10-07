# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    hash_ = dict()
    for i in arr:
        if i in hash_.keys():
            hash_[i] += 1
        else:
            hash_[i] = 1
    key = 0
    ans = 0
    list_data = list(hash_.items())

    def my_sort(e):
        return e[0]
    list_data.sort(key=my_sort)
    for item in list_data:
        index = item[0]
        check = item[1]
        if check > ans:
            key = index
            ans = check

    return key
