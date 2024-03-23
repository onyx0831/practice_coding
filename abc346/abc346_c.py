n, k = map(int, input().split())
a = set(map(int, input().split()))
ans = int(k*(k+1)//2)
for i in a:
    if i <= k:
        ans -= i
print(ans)

"""
競プロでは，意図的な入力による Hack を防ぐ方法として乱数を用いる方法が主流
https://atcoder.jp/contests/abc346/editorial/9635
import random
R = random.randint(1, 1 << 60)
N, K = map(int, input().split())
A = list(map(int, input().split()))
S = set([i ^ R for i in A]) # hack を防ぐため，i の代わりに i ^ R を用いる
ans = K*(K+1)//2
for j in S:
    i = j ^ R  # 元に戻す
    if i <= K:
        ans -= i
print(ans)
"""