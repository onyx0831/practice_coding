s = input()
t = input()

for i, s_c, t_c in zip(range(len(s)), s, t):
    if s_c != t_c:
        print(i+1)
        exit()
print(len(s)+1)