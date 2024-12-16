h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
ans = 0

for S in range(1 << (h+w-2)):
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