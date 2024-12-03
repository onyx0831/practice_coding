from collections import defaultdict
n = int(input())
q = int(input())

dict_2 = defaultdict(list)
dict_3 = defaultdict(set)

for _ in range(q):
    s = str(input())
    index = int(s.split()[0])
    if index == 1:
        i, j = int(s.split()[1]), int(s.split()[2])
        dict_2[j].append(i)
        dict_3[i].add(j)
    if index == 2:
        i = int(s.split()[1])
        print(*sorted(dict_2[i]))
    if index == 3:
        i = int(s.split()[1])
        print(*sorted(dict_3[i]))

# https://qiita.com/takkeybook/items/373b4f8330ef53a9594f