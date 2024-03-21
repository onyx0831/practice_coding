def sum_digits(j):
    return sum(int(d) for d in str(j))
"""
def digit_sum(n):
    # 整数 n の各桁の和を計算する関数
    return sum(map(int, str(n)))
"""
n, a, b = map(int,input().split())
ans = []
for i in range(1,n+1):
    c = sum_digits(i)
    if a <= c and c <= b:
        ans.append(i)
print(sum(ans))
