import re
s = input()
if re.fullmatch(r'\<[\=]+\>',s):
    print('Yes')
else:
    print('No')