r, c = map(int, input().split())
a = [[0 for _ in range(c+1)] for _ in range(r+1)]
for i in range(r):
    b = list(map(int,input().split()))
    for j in range(c):
        a[i][j] = b[j]
        a[r][j] += b[j]
    a[i][j+1] = sum(a[i])
a[r][c] = sum(a[r])

for i in range(r+1):
    print(*a[i])



