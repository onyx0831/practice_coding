n, l, r = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
    if a < l:
        ans.append(l)
    elif a >= r:
        ans.append(r)
    else:    
        ans.append(a)

print(*ans)
# https://atcoder.jp/contests/abc330/tasks/abc330_b
# 問題文意味不明
# 1つずつやるのが良い？