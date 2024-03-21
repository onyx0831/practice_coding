H, W = map(int, input().split())

list_h = [0 for _ in range(H)] # ここを予め用意
list_w = [0 for _ in range(W)] # ここを予め用意

for h in range(H):

    sum_h = 0
    a = str(input())
    for w in range(W):

        if a[w] == '#':
            sum_h += 1
            list_w[w] += 1
    
    list_h[h] = sum_h
    
ans_h = list_h.index(max(list_h)-1) + 1
ans_w = list_w.index(max(list_w)-1) + 1
print(f'{ans_h} {ans_w}')