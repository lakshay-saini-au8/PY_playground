#que https://www.hackerrank.com/challenges/python-string-formatting/problem
# solution
def print_formatted(number):
    # your code goes here
    w = len(bin(number).replace('0b',''))
    for i in range(1 , number+1):
        d = str(i).rjust(w," ")
        o = str(oct(i).replace('0o','')).rjust(w," ")
        h = str(hex(i).replace('0x','')).upper().rjust(w," ")
        b = str(bin(i).replace('0b','')).rjust(w," ")
        print(f"{d} {o} {h} {b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)