n = int(input())
A = list(map(int,input().split()))
sorted_A = sorted(A, reverse=True)#A.sort(reverse=Tru)
Alice = 0
Bob = 0
for i in range(len(sorted_A)):
    if i % 2 == 0:
        Alice += sorted_A[i]
    else:
        Bob += sorted_A[i]

print(Alice-Bob)