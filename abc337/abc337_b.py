# 拡張 ABC 文字列を表す正規表現は A*B*C*
from re import fullmatch
if fullmatch('A*B*C*', input()):
    print('Yes')
else:
    print('No')
