from collections import defaultdict
S=input()
N=len(S)
ans=0
count=defaultdict(int)

# 違う組がいくつできるか
for j in range(N):
    # aabbc
    # j=0のとき0-0回、j=1のときaが1回出てるので1-1回
    # j=2のとき2-0回、j=3のときbが1回出てるので3-1回
    # j=4のとき4-0回
    ans += j-count[S[j]]
    count[S[j]] += 1

# sと同じ文字列ができるか(同じ文字がある場合)
if max(count.values()) > 1:
    ans += 1

print(ans)