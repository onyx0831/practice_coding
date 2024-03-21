s = input()
t = input()
g = [[0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]]
d = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}

if g[d[s[0]]][d[s[1]]] == g[d[t[0]]][d[t[1]]]:
    print('Yes')
else:
    print('No')

"""
ABCDEAEDCBAに部分文字列として含まれている辺は短く、
そうでない辺は長いと判定できます
P = "ABCDEAEDCBA"
S = input()
T = input()
print("Yes" if (S in P) == (T in P) else "No")
"""