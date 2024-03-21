N = int(input())
A = list(map(int, input().split()))
l = [0] * N
indexA = {}

ans_list = []

for i, a in enumerate(A):
    l[a-1] += 1
    if l[a-1] == 2:
        indexA[a] = indexA.get(i+1, 0)

n_dict = dict(sorted(indexA.items(), key = lambda x : x[1]))
#print([i for i in n_dict.keys()])
print(" ".join(map(str, n_dict.keys())))
