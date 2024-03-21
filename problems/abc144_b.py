n = int(input())
kuku_set = set()
for i in range(1,10):
    for j in range(1,10):
        kuku_set.add(i*j)
if n in kuku_set:
    print('Yes')
else:
    print('No')