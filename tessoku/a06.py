N, Q = map(int, input().split())
A = list(map(int, input().split()))
# 累積を計算して持っておく
accum = [0] * (N + 1)
ans_list = []
for i in range(N):
    # 0 ~ A[i-1]番目の和
    accum[i+1] = accum[i] + A[i]

for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    ans = accum[r+1] - accum[l] 
    ans_list.append(ans)

for j in ans_list:
    print(j)
    