Sx, Sy = map(int,input().split())
Tx, Ty = map(int,input().split())
# スタート地点もゴール地点も、(2,1)状のタイルの左始まりに統一する
if (Sx + Sy) % 2 == 1:
    Sx -= 1
if (Tx + Ty) % 2 == 1:
    Tx -= 1

# 縦移動の回数abs(Sy - Ty), 横移動は縦移動と比較して多い方、max(abs(Sx - Tx), abs(Sy - Ty))、斜め移動は縦移動と横移動の合計の半分
res = (abs(Sy - Ty) + max(abs(Sx - Tx), abs(Sy - Ty))) // 2
print(res)
