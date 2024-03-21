# コンビネーション
MOD = 10**9 + 7
n, r = map(int, input().split())

# pが素数の時，mod pのとき
# 逆元ってどう求める，フェルマーの小定理，ユークリッドの互除法
# フェルマーの小定理 a^(p-1)=1(mod pで合同) , a^(p-2)=1/a(mod pで合同) 

def factorial(m):
    ans = 1
    for i in range(1, m+1):
        ans = ans * i % MOD
    return ans

def inv(m):
    return pow(m, MOD-2, MOD)

nCr = factorial(n) * inv(factorial(r) * factorial(n-r) % MOD) % MOD