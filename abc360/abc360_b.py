def slice_s_2_chars(s, j):
    n = len(s)
    slices = [s[i:i+j] for i in range(0, n, j)]
    return slices

s, t = input().split()
ls = len(s)
for i in range(1,ls):

    formed_t = slice_s_2_chars(s, i)
    
    for j in range(i):
        s_k = ""
        for k in formed_t:
            if len(k) > j:
                s_k += k[j]
        if s_k == t:
            print("Yes")
            quit()
print("No")
