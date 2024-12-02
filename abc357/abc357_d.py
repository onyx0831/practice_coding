def f(n, p):
    str_n = str(n)
    k = len(str_n)
    factor = 10 ** k

    if p == 1:
        return 0
    sum_geom = (pow(factor, n, p * (factor - 1)) - 1) // (factor - 1)
    sum_geom %= p

    result = (n * sum_geom) % p
    return result

MOD = 998244353
n = int(input())
result = f(n, MOD)
print(result)

