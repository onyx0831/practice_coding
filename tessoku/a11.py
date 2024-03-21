N, X = map(int, input().split())
A = list(map(int, input().split()))

# A.index(X)は全探索

# bottomに正解(X)が入ってほしい
# topに答えが入る場合A[mid]<K:bottom=mid, 0には到達しないことに注意
bottom, top = 0, N
while top - bottom > 1:
    # mid = (top + bottom) // 2 は危険，足すとオーバフローしたり負になったりする
    mid = bottom + (top - bottom) // 2

    if A[mid] > X:
        top = mid
    else:
        bottom = mid

print(bottom + 1)