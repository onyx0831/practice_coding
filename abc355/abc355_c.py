n, t = map(int,input().split())
A = list(map(int,input().split()))
d_t = {i: [] for i in range(n)} #縦がキー
d_y = {i: [] for i in range(n)} #横がキー
d_n1 = [] #斜め1がキー
d_n2 = [] #斜め2がキー

c = 0
for a in A:
    b = a - 1
    c += 1
    d_t[b//n].append(b%n)
    d_y[b%n].append(b//n)
    if (b//n) == (b%n):
        d_n1.append(b)
    if (b//n)+(b%n) == (n-1):
        d_n2.append(b)
    # 判定
    if len(d_t[b//n]) == n:
        # 縦揃う条件
        print(c)
        quit()
    elif len(d_y[b%n]) == n:
        # 横揃う条件
        print(c)
        quit()
    elif len(d_n1) == n or len(d_n2) == n:
        # 斜め揃う条件
        print(c)
        quit()

print(-1)