# くりかえし二乗法
A, B = map(int, input().split())

# a^bをmodで割った余りを求める（毎回計算してたら間に合わない）
def modpow(a, b, mod):
    if b == 0:
        # 1(mod1のときの対応もしとく)
        return 1 % mod
    if b % 2 == 0:
        # 偶数
        return modpow(a*a%mod, b//2, mod)
    if b % 2 == 1:
        # 奇数
        return modpow(a, b-1, mod) * a % mod
    
print(modpow(A, B, 10**9+7))

## pythonではpow(a, b, mod)の関数がある