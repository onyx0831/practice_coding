a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
A = [a, b, c, d, e]

for i in range(5):
    for j in range(5):
        if i!=j and A[j]-A[i] > k:
            print(':(')
            quit()
print('Yay!')