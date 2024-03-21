n = int(input())
p = list(map(int,input().split()))
rank_dict = {human: rank for rank, human in enumerate(p)}
ans = []
q = int(input())
for i in range(q):
    a, b = map(int,input().split())
    if rank_dict[a] < rank_dict[b]:
        ans.append(a)
    else:
        ans.append(b)
[print(ans[i]) for i in range(q)]
