import math

def is_square_number(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num ** 2 == num

n = int(input())
a = list(map(int, input().split()))
ans = 0
for i, v in enumerate(a):
    for w in a[i+1:]:
        if is_square_number(v*w):
            ans += 1
print(ans)