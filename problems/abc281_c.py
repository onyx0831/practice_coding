n, t = map(int, input().split())
A = list(map(int, input().split()))
A_sum = sum(A)
x = t // A_sum

if x >= 1:
    t -= A_sum * x

for i in range(n):
    rest = t
    t -= A[i]
    if t <= 0:
        print(f'{i+1} {rest}')
        quit()
