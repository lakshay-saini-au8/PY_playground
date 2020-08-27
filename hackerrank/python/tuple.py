#que https://www.hackerrank.com/challenges/python-tuples/problem
#solution

if __name__ == '__main__':
    n = int(input())
    print(hash(tuple(map(int,(input().split())))))
