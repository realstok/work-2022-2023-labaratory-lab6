import math 
from random import randint

def pollard(n: int) -> int:
    f = lambda x: (x**2 + 1) % n
    c = randint(0,n-1)
    a = c
    b = c
    while True:
        a = f(a)
        b = f(f(b))
        d = math.gcd(a-b, n)

        if 1 < d < n:
            return d
        elif d == n:
            return None

for i in range(10000, 10100):
    p = pollard(i)
    if p: print(i, p, i//p)
