n = int(input())
s = input()

chars = set(s)
if len(chars) == 1:
    print(-1)
else:
    max_len = max(len(x) for x in s.split('-'))
    print(max_len)

# 別解
# N, S = input(), input()
# print(max(map(len, S.split('-'))) if 'o' in S and '-' in S else -1)
