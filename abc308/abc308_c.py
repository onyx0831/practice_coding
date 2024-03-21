
from decimal import Decimal

N = int(input())
ans_dict = dict()

for i in range(N):
    a, b = map(Decimal, input().split())
    p = Decimal(a) / (Decimal(a) + Decimal(b))
    ans_dict[i+1] = p

ans = dict(sorted(ans_dict.items(), key = lambda x : x[1], reverse=True))
_ans = [i for i in ans.keys()]
print(*_ans)


"""

from functools import cmp_to_key
def cmp(a, b):
    x, y, i = a
    xx, yy, ii = b
    s = x * yy - y * xx
    return 1 if s > 0 else -1 if s < 0 else 0
 
n = int(input())
member_lists = []
for i in range(n):
    a, b = map(int, input().split())
    member_lists.append((i+1, a, b))
member_lists = sorted(member_lists, key = cmp_to_key(cmp))
print(" ".join([str(m[0]) for m in member_lists]))   
"""