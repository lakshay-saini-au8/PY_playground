# https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k != n):
                    result.append([i, j, k])

    print(result)

# https://practice.geeksforgeeks.org/problems/replace-all-0s-with-5/1


def convertFive(n):
    # Code here
    numberStr = str(n)
    result = ""
    for index, value in enumerate(numberStr):
        if value == "0":
            result = result+"5"
        else:
            result = result+value

    return int(result)


# print(convertFive(0))


# https://www.hackerrank.com/challenges/arrays-ds/problem
#!/bin/python3


# Complete the reverseArray function below.

def reverseArray(a):
    result = []
    for i in range(len(a)):
        result.append(a.pop())

    return result

# https://practice.geeksforgeeks.org/problems/third-largest-element/1


def thirdLargest(arr, n):
    if(n >= 3):
        arr.sort()
        return arr[n-3]
    else:
        return -1


print(thirdLargest([18, 21, 10], 3))
