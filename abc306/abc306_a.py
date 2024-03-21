N = int(input())
S = str(input())
ans = ''
for i in range(N):
    str = S[i::N] + S[i::N]
    ans += str
print(ans)
