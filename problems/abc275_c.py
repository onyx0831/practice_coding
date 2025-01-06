from itertools import combinations

S = [list(input()) for _ in range(9)]

coords = set()
for i in range(9):
  for j in range(9):
    if S[i][j] == "#":
      coords.add((i, j))

ans = 0
for c in combinations(coords, 4):
  res = set()
  for i in range(4):
    x, y = c[i]
    for j in range(i + 1, 4):
      xx, yy = c[j]
      
      res.add((xx - x) ** 2 + (yy - y) ** 2)
  
  if len(res) == 2:
    ans += 1

print(ans)

# combinationsの使い方理解する
# 4つの座標を選ぶ組み合わせを全探索する