while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        quit()

    cou = 0
    for i in range (1, n):
        for j in range(i+1, n+1):
            r = x - (i + j)
            if r > j and r <= n:
                if r != i and r != j:
                    cou += 1
    print(cou)

