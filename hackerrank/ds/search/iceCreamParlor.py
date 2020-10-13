def icecreamParlor(m, arr):
    new_arr = list(map(lambda x : x-m,arr))
    for i in range(len(arr)):
        for j in range(i+1,len(new_arr)):
            if new_arr[j]<0:
                if arr[i] == abs(new_arr[j]):
                    return [i+1,j+1]