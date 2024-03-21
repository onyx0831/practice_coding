n = int(input())
a = list(map(int,input().split()))
n_p = 0
for i in a:
    if i >= 0:
        n_p += i
    else:
        n_p -= (-1)*i
        if n_p < 0:
            n_p = 0
print(n_p)
