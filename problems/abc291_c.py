n = int(input())
S = input()
x = 0
y = 0
visited = set()
def move_to(x,y):
    if (x,y) in visited:
        return True
    else:
        visited.add((x,y))
        return False

for s in S:
    if move_to(x,y):
        print('Yes')
        exit()
    if s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    elif s == 'U':
        y += 1
    elif s == 'D':
        y -= 1

if move_to(x,y):    
    print('Yes')
else:
    print('No')
    