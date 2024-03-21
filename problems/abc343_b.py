n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
ans = []
for a in A:
    ans_row = []
    for i in range(len(a)):
        if a[i] == 1:
            ans_row.append(i + 1)
    ans.append(ans_row)

for i in range(n):
    print(*ans[i])
