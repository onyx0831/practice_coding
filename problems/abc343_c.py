n = int(input())
i = 0
ans = 0
# K = i**3, K <= n
while i**3 <= n: 
    s = str(i**3)
    # sとsを逆にした文字列が一緒か
    if s == s[::-1]:
        ans = i**3
    i += 1
print(ans)
