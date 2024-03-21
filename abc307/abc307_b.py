N = int(input())
S = []
for _ in range(N):
    S.append(str(input()))

for i, s in enumerate(S):
    for j, t in enumerate(S):
        if i == j:
            pass
        else:
            l = s+t
            if l == l[::-1]:
                print('Yes')
                exit()
print('No')


