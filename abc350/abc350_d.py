from sys import setrecursionlimit
setrecursionlimit(10**8)

def dfs(x):
    # check[x]を訪問済みにする
    C[x]=True
    
    res=1
    for nxt in G[x]:
        # xに隣接するすべての頂点nxtについて
        if not C[nxt]:
            # 訪問してない場合、再帰的に探索する
            res+=dfs(nxt)
    return res

n, m = map(int, input().split())
# 訪問したかのリスト
C=[False]*n
G = [[] for _ in range(n)]
for _ in range(m):
   a, b = map(int, input().split())
   a -= 1
   b -= 1
   G[a].append(b)
   G[b].append(a)

ans=-m # 辺の数
for i in range(n):
    if not C[i]:
        s=dfs(i)
        ans+=s*(s-1)//2
print(ans)


"""
4 3
1 2
2 3
1 4
"""
# [[1, 3], [0, 2], [1], [0]]
