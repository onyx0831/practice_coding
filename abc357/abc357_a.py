n,m = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(n):
    m -= A[i]
    ans += 1
    if m < 0:
        ans -= 1
        break
print(ans)