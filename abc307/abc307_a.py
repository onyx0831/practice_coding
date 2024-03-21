N = int(input())
A = list(map(int, input().split()))
ans = []
r = [i * 7 for i in range(1, N+1)]
r = [0] + r
for j in range(1, N+1):
    ans.append(sum(A[r[j-1]:r[j]]))

print(*ans)
