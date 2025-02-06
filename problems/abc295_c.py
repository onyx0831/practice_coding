n = int(input())
A = list(map(int, input().split()))

num_count = {}
for i in A:
    if i in num_count:
        num_count[i] += 0.5
    else:
        num_count[i] = 0.5

ans = 0
for count in num_count.values():
    ans += int(count)
print(ans)