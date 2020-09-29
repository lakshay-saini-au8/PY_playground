def group_anagrams(arr):
    n = len(arr)
    for i in range(n):
        sr = sorted(arr[i])
        arr[i] = "".join(sr)
    hash_ = dict()
    for index, value in enumerate(arr):
        if value in hash_.keys():
            hash_[value].append(index+1)
        else:

            hash_[f"{value}"] = [index+1]
    print(list(hash_.values()))


arr = ["cat", "dog", "god", "tca"]

group_anagrams(arr)
