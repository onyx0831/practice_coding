h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
ans = 0

# Sは進行方向を表すh+w-2ケタのビット列、全て列挙
for S in range(1 << (h+w-2)):
    # 下移動の回数がh-1回でない場合はスキップ
    if S.bit_count() != h-1:
        continue
    x, y = 0, 0
    good_path = True
    st = set()
    st.add(A[x][y])
    for i in range(h+w-2):
        if S >> i & 1:
            x += 1
        else:
            y += 1
        if A[x][y] in st:
            good_path = False
            break
        st.add(A[x][y])
    if good_path:
        ans += 1
print(ans)