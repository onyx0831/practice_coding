import copy
N = int(input())

A = []
B = []
for i in range(N):
    A.append(list(str(input())))
B = copy.deepcopy(A)
for i in range(N):
    
    for j in range(N):

        if (i == 0) and (j != 0):# 1行目の2~n
            B[i][j] = A[i][j-1] 
        
        elif (i != (N-1)) and (j == 0):# n行目以外の1
            B[i][j] = A[i+1][j]

        elif (i != 0) and (j == (N-1)):# 1行目以外のn
            B[i][j] = A[i-1][j]

        elif (i == (N-1) )and (j != (N-1)):# n行目のn以外
            B[i][j] = A[i][j+1]

for k in B:
    print("".join(k))
