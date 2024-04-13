from collections import defaultdict
d = defaultdict(list)
score = 0
n = int(input())
for _ in range(n):
    a, c = map(int, input().split())
    d[c].append(a)

for k,v in d.items():
    if min(v) > score:
        score = min(v)
print(score)