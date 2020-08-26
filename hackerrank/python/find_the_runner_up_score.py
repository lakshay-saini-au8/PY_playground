#  question https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#  solution

if __name__ == '__main__':
    n = int(input())
    l=  list(set(map(int,input().split())))
    l.sort(reverse=True)
    print(l[1])
    