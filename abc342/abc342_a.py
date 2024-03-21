s = input()
if s[0] == s[1]:
    for i in range(2,len(s)):
        if s[0] != s[i]:
            print(i+1)
            quit()
else:
    if s[0] == s[2]:
        print(2)
        quit()
    else:
        print(1)
        quit()

