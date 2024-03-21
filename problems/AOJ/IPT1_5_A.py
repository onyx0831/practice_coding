while True:
    h, w = map(int, input().split())
    if (h == 0) & (w == 0):
        break
    a = '#' * w
    for _ in range(h):
        print(a)