n = int(input())
A = list(map(int,input().split()))
ans = []

for i in A:
    ans.append(i)

    while len(ans) >= 2 and ans[-1] == ans[-2]:
        curr = ans.pop()
        ans.pop()
        ans.append(curr+1)
print(len(ans))
# while内の計算量が最悪O(n-1)が1回=総計算量はO(n)+O(n-1)
# 計算量が全く考慮できなかった。愚直にやるとO(n^2)かかると思った。
