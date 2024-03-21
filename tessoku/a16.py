N = int(input())
# 添え字の始まる場所に注意
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

# iまでに着く時間を記録
dp = [0] * N
for i in range(1, N):
    if i == 1:
        dp[i] = dp[i-1] + A[i]
    else:
        dp[i] = min(dp[i-1] + A[i], dp[i-2] + B[i])

print(dp[N-1])