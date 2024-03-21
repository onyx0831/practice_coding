q = int(input())
a = []
ans = []
for i in range(q):
    n, x = map(int, input().split())
    if n == 1:
        a.append(x)
    else:
        ans.append(a[-x])
[print(ans[i]) for i in range(len(ans))]