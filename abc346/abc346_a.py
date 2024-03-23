n = int(input())
a = list(map(int, input().split()))
b = [0] * (n-1)
for i in range(1,n):
    b[i-1] = a[i-1] * a[i]
print(*b)