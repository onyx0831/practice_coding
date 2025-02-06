from collections import defaultdict, deque
n = int(input())
g = defaultdict(list)

for i in range(n):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(1)
floor = {1}
while q:
    v = q.popleft()
    
    for i in g[v]:
        if not i in floor:
            q.append(i)
            floor.add(i)
    
print(max(floor))
