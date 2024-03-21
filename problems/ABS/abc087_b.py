
a = int(input())#500
b = int(input())#100
c = int(input())#50
x = int(input())#50の倍数
ans = 0
for i in range(a+1):
    for j in range(b+1):
        nokori = (x - (500*i + 100*j))
        if nokori >= 0 and nokori/50 <= c:
                ans += 1
print(ans)
