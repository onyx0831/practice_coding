# n番目に大きい:大きいほうからn番目か = list[-n]
def make_divisors(n):
    # 約数をlistで変えす
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

a, b, k = map(int, input().split())
a_b = set(make_divisors(a)) & set(make_divisors(b))
print(sorted(a_b)[-k])

# 単純にfor文(1~100)でa,bで割り切れたらiをリストに追加でよい