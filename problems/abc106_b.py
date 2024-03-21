n = int(input())
ans = 0
if n < 105:
    ans = 0
else:
    for i in range(105,n+1):
        c = 0
        if i % 2 == 1:
            for j in range(1, i+1):
                if i % j == 0:
                    c += 1
            if c == 8:
                ans += 1
print(ans)

