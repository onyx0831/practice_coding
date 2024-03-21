N,K=map(int,input().split())

AB=[]
ans=0

for _ in range(N):
    A,B=map(int,input().split())
    AB.append((A,B))
    ans+=B
AB.sort()

if(ans<=K):
    print(1)
    exit()

for i in range(N):
    ans-=AB[i][1]
    if(ans<=K):
        print(AB[i][0]+1)
        exit()

print(AB[N-1][0]+1)