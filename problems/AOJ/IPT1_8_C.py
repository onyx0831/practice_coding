import re
d = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
while True:
    try:
        s = input().strip()
        for c in s:
            if re.search('[a-z]',c.lower()):
                d[c.lower()] += 1
    except EOFError:
        break
for c, i in d.items():
    print(f'{c} : {i}')
"""
chr(): Unicodeコードポイントの文字を取得する
ord(): 文字のUnicodeコードポイントを取得する
re.search('[a-z]', hoge)
strip(): 文字列の両端（先頭、末尾）の指定した文字を削除する
デフォルトでは両端の連続する空白文字が取り除かれる
"""