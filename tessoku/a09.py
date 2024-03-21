H, W, N = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

ans = [[0] * (W+1) for _ in range(H)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    x2 += 1
    y2 += 1

    ans[x1][y1] += 1
    ans[x2][y1] -= 1
    ans[x1][y2] -= 1
    ans[x2][y2] += 1

for i in range(H):
    for j in range(W):
        if i - 1 >= 0:
            ans[i][j] += ans[i-1][j]

for i in range(H):
    for j in range(W):
        if j - 1 >= 0:
            ans[i][j] += ans[i][j-1]

for i in range(H):
    print(*ans[i][:-1])#配列を空白区切りで出力