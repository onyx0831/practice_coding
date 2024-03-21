# mod
"""
a*b=c
(a%m)*(b%m)%m=(c%m)
a*b 合同 C (mod m)
"""
N = int(input())
b = 0

for _ in range(N):
    T, A = input().split()
    A = int(A)
    if T == '+':
        b += A
    if T == '-':
        b -= A
    if T == '*':
        b *= A
    b %= 10000

print(b)


