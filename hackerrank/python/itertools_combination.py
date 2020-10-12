# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
string, value = input().split()
res_final = ["".join(sorted(i)) for i in list(
    combinations_with_replacement(string, int(value)))]
[print(i) for i in sorted(res_final)]
