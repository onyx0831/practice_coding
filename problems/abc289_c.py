n, m = map(int, input().split())
C = []
A = []
ans = 0
for _ in range(m):
    C.append(int(input()))
    A.append(list(map(int, input().split())))

# ビット全探索
# iは0から2^m-1までの整数、Aのどの要素を選ぶかを表す
for i in range(1 << m):
    # i = 0b1011の場合、j = 0, 1, 3が選ばれる, 0b0000はスキップ
    if i == 0:
        continue
    st = set()
    for j in range(m):
        # iのjビット目が立っている場合
        if i >> j & 1:
            # A[j]の要素を全て取って、setに入れる
            for k in range(C[j]):
                st.add(A[j][k])
    # 1~nまで全てを取れているか判定
    if len(st) == n:
        ans += 1
print(ans)
