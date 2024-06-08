# Sは英小文字および英大文字からなる文字列, Sの長さは1以上99以下の奇数
S = input()
# Sに含まれる大文字の数を数える
count = 0
for s in S:
    if s.isupper():
        count += 1
# Sに含まれる大文字の数がSの長さの半分以上ならば大文字に変換
if count > len(S) // 2:
    print(S.upper())
else:
    # そうでなければ小文字に変換
    print(S.lower())

