from collections import defaultdict

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
S = [list(row) for row in zip(*S)]  # 転置
T = [list(input()) for _ in range(H)]
T = [list(row) for row in zip(*T)]

s_dict = defaultdict(int)  # 連想配列でカラムの種類をカウント
t_dict = defaultdict(int)

for s_col, t_col in zip(S, T):
    s_dict["".join(s_col)] += 1
    t_dict["".join(t_col)] += 1

for col in s_dict.keys():
    if s_dict[col] != t_dict[col]:
        exit(print("No"))

print("Yes")