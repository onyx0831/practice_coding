s = input()
c = 0
r = 0
m = 0
for si in s:
    if si == 'R':
        r = c
    elif si == 'M':
        m = c
    c += 1

if r < m:
    print('Yes')
else:
    print('No')

