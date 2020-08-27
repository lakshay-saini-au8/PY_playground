#https://www.hackerrank.com/challenges/python-string-split-and-join/problem
#soltuion
def split_and_join(line):
    # write your code here
    sep = line.split(" ")
    return '-'.join(sep)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)