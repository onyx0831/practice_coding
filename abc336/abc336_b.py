n = int(input())
n_2 = "{:b}".format(n)
cou = 0
for i in n_2[::-1]:
    if i == '0':
        cou += 1
    else:
        print(cou)
        break
