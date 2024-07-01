n = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(n*2-2):
    if A[i] == A[i+2]:
        ans += 1
print(ans)
