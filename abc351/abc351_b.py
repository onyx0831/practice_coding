n = int(input())
A = [input() for _ in range(n)]
B = [input() for _ in range(n)]
c = 0
for a, b in zip(A, B):
    c += 1
    for i in range(n):
        if a[i] != b[i]:
            print(f'{c} {i+1}')
            quit()