n, a, b = map(int, input().split())
s = input()

ans = 10 ** 15
for i in range(n // 2):
    cnt = 0
    for j in range(n // 2):
        if s[i + j] == s[(n + i - j - 1) % n]:
            cnt += 1
    
    money =  i * a + (n // 2 - cnt) * b

    ans = min(ans, money)

print(ans)
