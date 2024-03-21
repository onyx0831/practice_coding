N = int(input())
a = N % 5
if a == 0:
    print(N)
elif a == 1 or a == 2:
    print(N-a)
else:
    print(N+(5-a))
