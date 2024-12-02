# 「998244353 で割ったあまり」の求め方

# 足し算、掛け算は基本的に計算の途中過程で積極的にあまりをとって良い
def add_mod(a, b, mod):
    return ((a % mod)+ b) % mod
def mul_mod(a, b, mod):
    return ((a % mod) * b) % mod
# 引き算は負の数のあまりに注意する
def sub_mod(a, b, mod):
    return (a%MOD - b%MOD) % mod


if __name__ == '__main__':
    MOD = 998244353
    a = 998244000
    b = 500
    print(add_mod(a, b, MOD)) #20147
    print(mul_mod(a, b, MOD)) #9823500
    c = 998245000
    d = 5000
    print(sub_mod(c, d, MOD)) #998240000
    