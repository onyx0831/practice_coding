from string import ascii_lowercase
c2c = {c: 0 for c in ascii_lowercase}
s = input()
for c in s:
    c2c[c] += 1
print(max(c2c.items(), key=lambda x: x[1])[0])