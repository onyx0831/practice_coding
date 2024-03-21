n = int(input())
s = input()
ans = 0
for i in range(3, n+1):
    if s[i-3:i] == 'ABC':
        ans += 1
print(ans)