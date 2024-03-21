p, q = map(str, input().split())
list_sum = [0, 3, 4, 8, 9, 14, 23]
map_en = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6,}

map_p = map_en[p]
map_q = map_en[q]

if map_p < map_q:
    print(list_sum[map_q] - list_sum[map_p])
else:
    print(list_sum[map_p] - list_sum[map_q])