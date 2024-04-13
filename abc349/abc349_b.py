from collections import Counter
s = input()
c = Counter(s)
ans_list = [2]*100
for k,v in c.items():
    #print(k, v)
    ans_list[v-1] -= 1
for i in ans_list:
    if i == 0 or i == 2:
        pass
    else:
        print('No')
        quit()
print('Yes')