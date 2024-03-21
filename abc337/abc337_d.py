h, w, k = map(int,input().split())
f =  [list(input()) for _ in range(h)]
INF = 10**10
ans = INF

for l in f:
    if len(l) < k:
        continue
    o = 0
    x = 0

    # 行のoとxを数える
    for i in range(k):
        if l[i] == 'o':
            o += 1
        if l[i] == 'x':
            x += 1
    if x == 0:
        ans = min(ans, k-o)
    
    # k個横にずらして、数を更新
    for i in range(k, len(l)):
        if l[i] == 'o':
            o += 1
        if l[i] == 'x':
            x += 1
        if l[i-k] == 'o':
            o -= 1
        if l[i-k] == 'x':
            x -= 1
        if x == 0:
            # k-oがdotの数
            ans = min(ans, k-o)

f = zip(*f)

for l in f:
    if len(l) < k:
        continue
    o = 0
    x = 0

    for i in range(k):
        if l[i] == 'o':
            o += 1
        if l[i] == 'x':
            x += 1
    if x == 0:
        ans = min(ans, k-o)
        
    for i in range(k, len(l)):
        if l[i] == 'o':
            o += 1
        if l[i] == 'x':
            x += 1
        if l[i-k] == 'o':
            o -= 1
        if l[i-k] == 'x':
            x -= 1
        if x == 0:
            ans = min(ans, k-o)
if ans == INF:
    print(-1)
else:
    print(ans)
"""
1行W列のグリッドが与えられたときに、
グリッド内で横方向にoをK個並べることは可能か？
可能ならその最小手数は？
という問題を O(W) 時間で解くことを考える

横みて、転置して最小を取る

"""
