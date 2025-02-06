n = int(input())
s = input()
cnt = 0
ans_s = ''
for c in s:
    if c == '\"' and cnt == 0:
        cnt = 1
    elif c == '\"' and cnt == 1:
        cnt = 0
    if c == ',' and cnt == 0:
        ans_s += '.'
    else:
        ans_s += c
print(ans_s)
