import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
visited = [False] * n
cnt = 0

def dfs(x):
    global visited, g
    if visited[x]:
        return
    visited[x] = True
    for i in g[x]:
        dfs(i)

for i in range(n):
    # グラフの連結成分の個数を数える
    if not visited[i]:
        dfs(i)
        cnt += 1
# 閉路ができないようになるため、最小の辺の数はm - n + cnt
print(m - n + cnt)