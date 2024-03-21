n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
l = int(input())
C = list(map(int,input().split()))
q = int(input())
X = list(map(int,input().split()))

min_x = min(A) + min(B) + min(C)
max_x = max(A) + max(B) + max(C)
abc = set()
for i in range(n):
    for j in range(m):
        for k in range(l):
            abc.add(A[i] + B[j] + C[k])

for x in X:
    if min_x > x or max_x < x:
        print('No')
    else:
        if x in abc:
            print('Yes')
        else:
            print('No')