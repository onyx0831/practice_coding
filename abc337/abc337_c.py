n = int(input())
a =  list(map(int,input().split()))
d = {value: index+1 for index, value in enumerate(a)}
ans = []
t = 0
for i in range(n):
    if i == 0:
        t = d.get(-1)
        ans.append(t)
    else:
        t = d.get(t)
        ans.append(t)

print(*ans)
