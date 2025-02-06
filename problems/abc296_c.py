n, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
i = 0
for j in range(n):
    print(f'j:{j}')
    while i < n and A[i] - A[j] < x:
        print(f'i:{i}')
        i += 1
    if i < n and A[i] - A[j] == x:
        print('Yes')
        quit()
print('No')
# 尺取り法のイメージがつかめるか