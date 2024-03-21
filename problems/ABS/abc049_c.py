s = input().strip()[::-1]
words = ['dream', 'dreamer', 'erase', 'eraser']
words = [word[::-1] for word in words]
# 後ろから見る
while len(s) > 0:
    match = False
    for w in words:
        # 文字列が指定した引数の検索する文字列で始まっていればtrueを返し、そうでない場合はfalseを返す
        if s.startswith(w):
            s = s[len(w):]
            match = True
            break
    if not match:
        break
if len(s) == 0:
    print('YES')
else:
    print('NO')