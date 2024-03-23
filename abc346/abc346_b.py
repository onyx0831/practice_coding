w, b = map(int, input().split())
s = 'wbwbwwbwbwbw'*40
for i in range(12):
    c = i
    w_c = 0
    b_c = 0
    while True:
        if s[c] == 'w':
            w_c += 1
        else:
            b_c += 1

        if w == w_c and b == b_c:
            print('Yes')
            quit()
        elif w < w_c or b < b_c:
            break
        else:
            c += 1

print('No')