# DP
n = int(input())
A = list(map(int, input().split()))
grundy = 0

for a in A:
    grundy ^= a

if grundy == 0:
    print('Second')
else:
    print('First')

