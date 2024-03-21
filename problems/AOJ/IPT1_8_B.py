while True:
    x=input()
    if x == '0':
        quit()
    ans = 0
    for i in x:
        ans += int(i)
    print(ans)

