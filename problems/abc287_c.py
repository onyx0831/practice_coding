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
visited = set()

def dfs(x):
    global visited, g
    if x in visited:
        return
    visited.add(x)
    for i in g[x]:
        dfs(i)

# 辺がちょうどN−1本
if m != (n-1):
    print("No")
    exit()

# 全ての頂点の次数が2以下の確認
for i in range(n):
    if len(g[i]) > 2:
        print("No")
        exit()

# グラフが連結かの確認
dfs(0)
if len(visited) != n:
    print("No")
    exit()
print("Yes")
