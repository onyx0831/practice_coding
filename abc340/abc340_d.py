# https://atcoder.jp/contests/abc340/submissions/50185824
# https://qiita.com/ell/items/fe52a9eb9499b7060ed6

"""
dp[1][0] = dp[0][0]+100, dp[1][1] =  dp[0][0]+200 to 3
dp[2][0] = dp[1][0]+50, dp[2][1] = dp[1][0]+10 to 1
dp[3][0] = dp[2][0]+100 or dp[1][1]+100, dp[3][1] = dp[2][0]+200 or dp[1][1]+200, to5
"""