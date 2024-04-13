n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = []
for i in range(n):
    pre_ans = []
    for j in range(n):
        d = ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)**0.5
        pre_ans.append(d)
    ans.append(pre_ans.index(max(pre_ans))+1)

[print(ans[i]) for i in range(n)]