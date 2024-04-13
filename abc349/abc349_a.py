n = int(input())
A = list(map(int,input().split()))
ans = 0
for i in A:
    ans += i
ans = ans * -1
print(ans)