n = int(input())
A = list(map(int, input().split()))
A_set = set(A)
A_set_sort = sorted(A_set)

print(A_set_sort[-2])