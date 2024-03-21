def count_division_two(n:int)->int:
    c = 0
    while n > 0:
        if n % 2 == 1:
            return c
        else:
            n /= 2
            c += 1

INF = 10 ** 10
nn = int(input())
A = list(map(int,input().split()))
ans = INF
for i in A:
    ans = min(ans, count_division_two(i))
print(ans)
# 2の何乗かを調べて、一番小さい数を出す