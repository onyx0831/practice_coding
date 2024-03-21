# 素数判定
# 素数表がある場合，試し割をする場合

Q = int(input())
for _ in range(Q):
    x = int(input())
    d = 2
    while d * d <= x:
        if x % d == 0:
            print('No')
            break
        d += 1
    else:
        # break以外で脱出した場合，ここにくる
        print('Yes')