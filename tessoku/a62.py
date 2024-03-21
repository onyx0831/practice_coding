# DFS
from sys import setrecursionlimit
setrecursionlimit(10**7)

N, M = map(int, input().split())
# 隣接リスト
edge = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

come = [False] *(N+1)

def dfs(x):
    come[x] = True
    for to in edge[x]:
        if come[to]:
            continue
        dfs(to)

dfs(1)

if all[come[1:]]:
    print("The graph is connected.")
else:
    print("The graph is not connected.")