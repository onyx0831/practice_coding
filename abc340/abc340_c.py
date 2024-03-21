from sys import setrecursionlimit
setrecursionlimit(10**8)

N = int(input())
d = dict()
d[1] = 0
d[2] = 2

def func(x):
    global d
    if x in d:return d[x]
    #if x == 1: return 0
    #if x == 2: return 2
    if x % 2 == 1:
        a = x // 2 + 1
        b = x // 2
    elif x % 2 == 0:
        a = x // 2
        b = x // 2
    d[x] = x + func(a) + func(b)
    return d[x]

print(func(N))

"""
from functools import lru_cache
import sys
sys.setrecursionlimit(10**9)
import pypyjit
pypyjit.set_param("max_unroll_recursion=-1")

@lru_cache(maxsize=10**17)
def rec(n):
    if n == 1:
        return 0
    else:
        return n+rec(n//2)+rec((n+1)//2)

n = int(input())

print(rec(n))
"""


# https://qiita.com/kotaroooo0/items/4d471932e299edd08b24
# https://qiita.com/shoji9x9/items/e7d19bd6f54e960f46be

