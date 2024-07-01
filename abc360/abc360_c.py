n = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

# Aがkey, Wがvalueの辞書を作成, {2:[13, 14], 3:[15, 16, 17]}
dic = {}
for i in range(n):
    if A[i] in dic:
        dic[A[i]].append(W[i])
    else:
        dic[A[i]] = [W[i]]

# 各valueの要素の、maxの値を取ってsum(W)から引いていく
ans = sum(W)
for key in dic:
    ans -= max(dic[key])

print(ans)
"""
自分の方針
要素が2つ以上あるものの中から、最小のものを取り除いて行って、取り除いたものを足し合わせる
最終的に要素が1つになるまで繰り返す
を各keyごとに行えば良いと考えたが、それだと計算量がO(n^2)になってしまった。
解説の方針
各keyごとに、valueの最大値をsum(W)から引くことで、最終的に最小のコストがわかる
"""