n, y = map(int, input().split())

for i in range(n+1):
    yukichi = 10000*i
    for j in range((n+1)-i):
        higuchi = 5000*j

        k = (y - (yukichi + higuchi)) // 1000
        if k == (n-(i+j)):
            print(f'{i} {j} {k}')
            quit()
        
print(f'-1 -1 -1')