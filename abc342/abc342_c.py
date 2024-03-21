from string import ascii_lowercase
c2c = {c: c for c in ascii_lowercase}
n = int(input())
s = input()
q = int(input())

for i in range(q):
    c, d = map(str,input().split())
    c2c[c] = d

print(s.translate(str.maketrans(c2c)))


# https://hibiki-press.tech/python/str-translate/5322