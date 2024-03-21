# DP
n, a, b = map(int, input().split())

# 先手が勝つか，dp[0]=False, dp[i]=dp[i-a] or dp[i-b]どっちかがfalseならtrue, どっちもtrueならfalse
# 
dp = [False] * (n+1)
for i in range(a):
    dp[i] = False

for i in range(a, n+1):
    dp[i] = False

    for j in [a, b]:
        nxt = i - j
        if nxt < 0:
            continue
        if not dp[nxt]:
            dp[i] = True

if dp[n]:
    print('First')
else:
    print('Second')