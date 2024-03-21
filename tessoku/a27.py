# ユークリッドの互除法
# 2つの変数の最大公約数を求める

def gcd(x, y):
    if x == 0:
        return y
    # 余りと残り，場所は入れ替わる
    return (y % x, x)

A, B = map(int, input().split())
print(gcd(A, B))
