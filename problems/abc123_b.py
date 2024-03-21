# 順列全探索
import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

A = [a, b, c, d, e]
ans = 10000000
ptn = list(itertools.permutations(A))
for p in ptn:
    t = 0
    #ex(29, 20, 7, 35, 120)
    for i in p[:-1]:
        yasumi = 0
        if i%10!=0:
            yasumi = 10-(i%10)
        t += i+yasumi
    t += p[4]
    ans = min(t, ans)
print(ans)
    
