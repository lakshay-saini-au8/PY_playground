# https://www.hackerrank.com/challenges/polar-coordinates/problem

import cmath

eq = input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))

print(pa)
print(r)
