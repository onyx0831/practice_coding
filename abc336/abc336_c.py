n = int(input())
n = n - 1
ans = ''
if n == 0:
    print(0)
    exit()
while n > 0:
    ans += str(n%5)
    n = n // 5
print(int(ans[::-1])*2)
