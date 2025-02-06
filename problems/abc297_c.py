h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w-1):
        if S[i][j] == 'T' and S[i][j+1] == 'T':
            S[i][j] = 'P'
            S[i][j+1] = 'C'

for k in range(h):
    print(''.join(S[k]))

# 文字列でなく、配列で管理すれば要素の変更が可能