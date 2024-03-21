h,w,n = map(int,input().split())
a = [['.']*w for _ in range(h)]
x = 0
y = 0
ehou = 0
for i in range(n):
    if a[y][x] == '#':
        a[y][x] = '.'
        if ehou == 0:
            ehou = 3
            x -= 1
            if x < 0:
                x = w-1
            
        elif ehou == 1:
            ehou = 0
            y -= 1
            if y < 0:
                y = h-1
            
        elif ehou == 2:
            ehou = 1
            x += 1
            if x >= w:
                x = 0
            
        elif ehou == 3:
            ehou = 2
            y += 1
            if y >= h:
                y = 0
            

    elif a[y][x] ==".":
        a[y][x] = '#'
        if ehou == 0:
            ehou = 1
            x += 1
            if x >= w:
                x = 0
            
        elif ehou == 1:
            ehou = 2
            y += 1
            if y >= h:
                y = 0
            
        elif ehou == 2:
            ehou = 3
            x -= 1
            if x < 0:
                x = w-1
            
        elif ehou == 3:
            ehou = 0
            y -= 1
            if y < 0:
                y = h-1
            

for i in a:
    print(''.join(i))