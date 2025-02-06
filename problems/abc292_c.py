from collections import defaultdict
n = int(input())

n_list = defaultdict(int)
for i in range(1, n):
    for j in range(1, n):
        if i * j >= n:
            break
        n_list[i*j] += 1
ans = 0
for num, count in n_list.items():
    rest = n - num
    if rest in n_list:
        ans += count * n_list[rest]
print(ans)

# https://atcoder.jp/contests/abc292/submissions/60232086
# https://drken1215.hatenablog.com/entry/2023/05/16/230900