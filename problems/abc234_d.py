import heapq
n, k = map(int, input().split())
P = list(map(int,input().split()))

# 1番目
que = P[0:k]
print(min(que))
heapq.heapify(que)
# 2番目以降
for i in range(k, n):
    min_mae = heapq.heappop(que)
    # 大きいほうを代入
    max_ima = max(min_mae, P[i])
    heapq.heappush(que, max_ima)
    # 今のmin(K番目)を取ってくる
    ans = heapq.heappop(que)
    heapq.heappush(que, ans)
    print(ans)