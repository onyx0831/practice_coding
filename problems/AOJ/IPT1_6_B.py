cards = [[False for i in range(13)] for j in range(4)] # 縦4横13の初期値Falseの配列
pattern = ["S", "H", "C", "D"] # 0:S, 1:H, 2:C, 3:D

n = int(input())
for _ in range(n):
    patt, num = map(str,input().split())
    cards[pattern.index(patt)][int(num)-1] = True
# 出力
for i in range(4):
    for j in range(13):
        if cards[i][j] == False:
            print(pattern[i], j+1)
