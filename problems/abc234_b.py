def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

n = int(input())
X = []
Y = []
ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(n):
    for j in range(i, n):
        d = distance(X[i], Y[i], X[j], Y[j])
        ans = max(ans, d)
print(ans)