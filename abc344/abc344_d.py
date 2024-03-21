t = input()
n = int(input())
A = []
S = []

for _ in range(n):
    x = input().split()
    A.append(int(x[0]))
    S.append(x[1:])

for s in S:
    