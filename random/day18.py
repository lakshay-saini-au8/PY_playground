def xor_sum(a, b):
    result = []
    total_sum = None
    for i in a:
        for j in b:
            result.append(i+j)
    total_sum = result[0]
    for k in range(1, len(result)):
        total_sum = total_sum ^ result[k]

    print(total_sum)


xor_sum([4, 6, 0, 0, 3, 3], [0, 5, 6, 5, 0, 3])


x = 2
y = 3
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(y << 1)
print(x >> 1)
