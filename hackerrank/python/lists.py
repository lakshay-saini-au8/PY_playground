#que https://www.hackerrank.com/challenges/python-lists/problem
#solution

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command , *line = input().split()
        args = list(map(int,line))
        if command == "insert":
            i,e = args
            l.insert(i,e)
        elif command == "print":
            print(l)
        elif command == "remove":
            l.remove(args[0])
        elif command == "append":
            l.append(args[0])
        elif command == "sort":
            l.sort()
        elif command == "pop":
            l.pop()
        elif command == "reverse":
            l.reverse()

