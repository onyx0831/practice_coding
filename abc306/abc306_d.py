N = int(input())
INF = 10**18
dp = [[-INF, -INF] for _ in range(N+1)]

for n in range(N+1):
    if n == 0:
        dp[0][0] = 0

    else:
        x, y = map(int, input().split())
        if x == 0:
            
            dp[n][0] = max(dp[n-1][0], dp[n-1][0]+ y, dp[n-1][1] + y) # 一個前が腹痛状態もこっちにいれる
            dp[n][1] =  dp[n-1][1] # 食べない選択

        else:
            # x == 1
            dp[n][0] = dp[n-1][0] # 食べない選択
            dp[n][1] = max(dp[n-1][1], dp[n-1][0] + y) # 一個前の腹痛か，一個前の元気＋食べるか

ans = max(dp[N][0], dp[N][1])
print(ans)


