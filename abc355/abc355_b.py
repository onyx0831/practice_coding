
n, m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A.copy()+B.copy()
A = sorted(A)
C = sorted(C)

for i in range(n-1):
    index = C.index(A[i])
    if C[index+1] == A[i+1]:
        print('Yes')
        quit()

print('No')