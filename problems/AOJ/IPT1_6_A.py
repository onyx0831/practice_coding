n = int(input())
a = list(map(int,input().split()))

_a = a[::-1]# a.reverse()でも可
print(" ".join(map(str, _a)))

"""
lst = [24, 16, 38]

for i, elem in enumerate(lst):
    print(i, elem)

# 0 24
# 1 16
# 2 38

lst = [10, 20, 30, 40, 50]
print(lst)
print("".join(map(str,lst)))    # 1020304050
print(" ".join(map(str,lst)))   # 10 20 30 40 50
print(",".join(map(str,lst)))   # 10,20,30,40,50

"""