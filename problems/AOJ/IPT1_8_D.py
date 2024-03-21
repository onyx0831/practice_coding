s = input()
p = input()
for i in range(len(s)):
    _s = s[i:len(s)] + s[0:i]
    if p in _s:
        print('Yes')
        quit()
print('No')
