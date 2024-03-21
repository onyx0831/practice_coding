A, B = map(int, input().split())

if A in [3, 6, 9]:
    print('No')
else:
    if A + 1 == B:
        print('Yes')
    else:
        print('No')