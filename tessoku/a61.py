# 

N, M = map(int, input().split())
# 隣接リスト
edge = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

for i in range(1, N+1):
    print("{}: {}".format(i, str(edge[i])
                                 .replace('[', '{')
                                 .replace(']', '}')
                                 ))
