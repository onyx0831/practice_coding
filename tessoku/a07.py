D = int(input())
N = int(input())

# 前日からの人数の差分をもつ
diff = [0] * (D+1)

for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    diff[l] += 1
    diff[r+1] -= 1
cou = 0
for i in range(D):
    cou += diff[i]
    print(cou)