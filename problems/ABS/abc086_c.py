n = int(input())
prev_t, prev_x, prev_y = 0, 0, 0

for _ in range(n):
    t, x, y = map(int, input().split())
    dist = abs(x-prev_x) + abs(y-prev_y)
    time_diff = t - prev_t

    if dist > time_diff or (time_diff-dist)%2 != 0:
        print('No')
        quit()

    prev_t, prev_x, prev_y = t, x, y

print('Yes')