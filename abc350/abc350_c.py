from copy import copy
def count_swaps_to_sort(A):
    B = copy(A)
    swaps = 0
    N = len(B)
    
    for i in range(N):
        while B[i] != i + 1:
            j = B[i] - 1
            B[i], B[j] = B[j], B[i]
            swaps += 1
            ans.append(f'{i+1} {j+1}')
    
    return swaps

n = int(input())
A = list(map(int, input().split()))
# A = [3, 4, 2, 1, 5]
ans = []
swaps_needed = count_swaps_to_sort(A)
print(swaps_needed)
for i in range(swaps_needed):
    print(ans[i])

