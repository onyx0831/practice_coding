A = []
while True:
    try:
        A.append(input())
    except:
        break
A = A[::-1]
[print(A[i]) for i in range(len(A))]