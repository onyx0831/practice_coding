s = input()
n = len(s)
c = 0
wo = False
for i in range(n-1):
    if wo:
        wo = False
        continue

    if s[i] == "0" and s[i+1] == "0":
        c += 1
        wo = True
print(n-c)