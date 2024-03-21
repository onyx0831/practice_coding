N = int(input())
ans = [0] * 10

# N - (2**i)ができるかをみる
# できるなら引き算してi番目を1にする
for i in range(9, -1, -1):
    if N - (2**i) >= 0:
        N -= (2**i)
        ans[i] = 1
ans = ans[::-1]#ans.reverse()
print(''.join(list(map(str, ans))))

# format(N, 'b') '0x'で16進数
