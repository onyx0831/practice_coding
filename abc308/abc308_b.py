N, M = map(str, input().split())
C = list(map(str, input().split()))
D = list(map(str, input().split()))
P = list(map(int, input().split()))

ans = 0
D = ['other'] + D
menu = dict(zip(D,P))

for c in C:
    if c in D:
        ans += menu[c]
    else:
        ans += menu['other']

print(ans)
