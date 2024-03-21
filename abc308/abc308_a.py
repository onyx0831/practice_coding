S = list(map(int, input().split()))
a = 0

for s in S:
    if (s >= 100) and (s <= 675):
        if s % 25 == 0:
            if a <= s:
                a = s
            else:
                print('No')
                exit()
        else:
            print('No')
            exit()
    else:
        print('No')
        exit()

print('Yes')
