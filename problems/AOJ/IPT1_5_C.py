while True:
    h, w = map(int, input().split())
    if (h == 0) & (w == 0):
        break
    # 縦足す横が偶数：#奇数：.

    for i in range(h):
        for j in range(w):
            if (i + j)%2 == 0:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()