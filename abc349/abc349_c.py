
from collections import deque
s = list(input().upper())
d = deque(s)
t = input()
i = 0
while len(d) != 0:
    c = d.popleft()
    if i < 2:
        if t[i] == c:
            i += 1
    elif i == 2:
        if t[i] == 'X' or t[i] == c:
            print('Yes')
            quit()
        else:
            pass
if i == 2 and t[2] == 'X':
    print('Yes')
    quit()
print('No')
# narita
# NRT
# RNTがダメだと分からなかった
# AAXのときをかんがえていなかった