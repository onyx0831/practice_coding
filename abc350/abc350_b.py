n, q = map(int, input().split())
T = list(map(int,input().split()))
ans = n
h = [0]*1001
for t in T:
    h[t] += 1
    if h[t] % 2 == 0:
        ans += 1
    else:
        ans -= 1

print(ans)