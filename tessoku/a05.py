N , k= map(int, input().split())
ans = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if 1 <= k-(i+j) <= N:
            ans += 1
print(ans)